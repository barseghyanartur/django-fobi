# from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpRequest
from django.utils.translation import ugettext

from nine import versions

from rest_framework import mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ....constants import (
    CALLBACK_BEFORE_FORM_VALIDATION,
    CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
    CALLBACK_FORM_VALID,
    CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
    CALLBACK_FORM_INVALID
)
from ....models import FormEntry

from .base import (
    fire_form_callbacks,
    run_form_handlers,
    submit_plugin_form_data,
)
from .dynamic import get_declared_fields
from .metadata import FobiMetaData
from .serializers import FormEntrySerializer
from .utils import get_serializer_class

__title__ = 'fobi.contrib.apps.drf_integration.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiFormEntryViewSet',)


class FobiFormEntryViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    """FormEntry view set."""
    # By definition of this app we have only list, detail and update actions.
    # In update action we are going to handle form entry creation.
    # In case of self.action == 'update' or 'partial_update' we do need to
    # show dynamic serializer of the form fields (not of the model).
    # In all other cases, we need to show serializer of the model (which is
    # simply one field - model slug).

    queryset = FormEntry.objects.filter(is_public=True).select_related('user')
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    metadata_class = FobiMetaData

    def has_value(self):
        return None if self.action == 'metadata' else True

    def get_queryset(self):
        """Get queryset.

        We show all forms to authenticated users and show only public forms
        to non-authenticated users.
        """
        if versions.DJANGO_GTE_1_10:
            user_is_authenticated = self.request.user.is_authenticated
        else:
            user_is_authenticated = self.request.user.is_authenticated()
        kwargs = {}
        if not user_is_authenticated:
            kwargs.update({'is_public': True})
        return FormEntry.objects.select_related('user').filter(**kwargs)

    def get_object(self):
        """Override get_object to get things done."""
        obj = super(FobiFormEntryViewSet, self).get_object()

        # OK, calling this twice sucks, but fine for the time being.
        # In future we should try to get rid of additional queries
        # made double.
        declared_fields, declared_fields_metadata = get_declared_fields(
            obj,
            has_value=self.has_value()
        )

        # Setting all the fields, one by one like they were attributes of
        # the object (while they are obviously NOT). It's all done just to
        # trick the rest_framework and make a profit of all the nice things
        # it provides with as little efforts as possible. However, we NEVER
        # save the object.
        for field_name, field_instance in declared_fields.items():
            setattr(obj, field_name, field_instance.initial)

        # Return "patched" object.
        return obj

    def get_serializer(self, *args, **kwargs):
        """Get the serializer."""
        if self.action in ('update', 'partial_update', 'metadata'):
            serializer_class = self.get_serializer_class()
            # kwargs['context'] = {'request': self.request}
            kwargs['context'] = self.get_serializer_context()
        else:
            serializer_class = FormEntrySerializer
            # kwargs['context'] = {'request': self.request}
            kwargs['context'] = self.get_serializer_context()

        serializer = serializer_class(*args, **kwargs)

        # if 'data' in kwargs:
        #     serializer.is_valid()

        return serializer

    def get_serializer_class(self):
        """Get serializer class."""
        form_entry = self.get_object()
        serializer_class = get_serializer_class(
            form_entry=form_entry,
            request=self.request,
            has_value=self.has_value()
        )
        return serializer_class

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        # Handle submitted form data by firing form handler plugins.
        self._handle_form_entry_data_submission(
            form_entry=instance,
            request=request,
            serializer=serializer
        )

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def _handle_form_entry_data_submission(self,
                                           form_entry,
                                           request,
                                           serializer):
        """Handle form entry data submission."""
        # Try to fetch only once.
        form_element_entries = form_entry.formelemententry_set.all()

        # Fire form valid before submit plugin data
        serializer = fire_form_callbacks(
            form_entry=form_entry,
            request=request,
            serializer=serializer,
            stage=CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA
        )

        # Fire plugin processors
        serializer = submit_plugin_form_data(
            form_entry=form_entry,
            request=request,
            serializer=serializer
        )

        # Fire form valid callbacks
        serializer = fire_form_callbacks(
            form_entry=form_entry,
            request=request,
            serializer=serializer,
            stage=CALLBACK_FORM_VALID
        )

        # Run all handlers
        handler_responses, handler_errors = run_form_handlers(
            form_entry=form_entry,
            request=request,
            serializer=serializer,
            form_element_entries=form_element_entries
        )

        # Warning that not everything went ok.
        if handler_errors:
            _request = request \
                if isinstance(request, HttpRequest) \
                else request._request
            for handler_error in handler_errors:
                messages.warning(
                    _request,
                    ugettext("Error occurred: {0}.").format(handler_error)
                )

        # Fire post handler callbacks
        fire_form_callbacks(
            form_entry=form_entry,
            request=request,
            serializer=serializer,
            stage=CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS
        )
