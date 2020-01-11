from django import forms
from django.conf import settings
from django.forms.utils import ErrorDict
from django.template import Library, TemplateSyntaxError, Node
from django.utils.translation import gettext_lazy as _

from ..base import get_theme
from ..settings import DISPLAY_AUTH_LINK

__title__ = 'fobi.templatetags.fobi_tags'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_fobi_form_handler_plugin_custom_actions',
    'get_fobi_form_wizard_handler_plugin_custom_actions',
    'get_fobi_plugin',
    'get_form_field_type',
    'get_form_hidden_fields_errors',
    'has_edit_form_entry_permissions',
    'render_auth_link',
    'render_fobi_forms_list',
)

THEME = get_theme(request=None, as_instance=True)

register = Library()

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** General Fobi tags ******************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# ******************************* Plugin specific *****************************
# *****************************************************************************


class GetFobiPluginNode(Node):
    """Node for ``get_fobi_plugin`` tag."""

    def __init__(self, entry, as_var=None):
        """Constructor."""
        self.entry = entry
        self.as_var = as_var

    def render(self, context):
        """Render."""
        request = context['request']
        entry = self.entry.resolve(context, True)

        plugin = entry.get_plugin(request=request)
        context[self.as_var] = plugin
        return ''


@register.tag
def get_fobi_plugin(parser, token):
    """Get the plugin.

    Note, that ``entry`` shall be a instance of
    ``fobi.models.FormElementEntry`` or ``fobi.models.FormHandlerEntry``.

    :syntax:

        {% get_fobi_plugin entry as [context_var_name] %}

    :example:

        {% get_fobi_plugin entry as plugin %}

        {% get_fobi_plugin entry as plugin %}
        {{ plugin.render }}
    """
    bits = token.contents.split()

    if len(bits) == 4:
        if bits[-2] != 'as':
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(
                    bits[0]
                )
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid "
            "syntax.".format(bits[0])
        )

    entry = parser.compile_filter(bits[1])

    return GetFobiPluginNode(entry=entry, as_var=as_var)

# *****************************************************************************
# ********************** Form handler plugin specific *************************
# *****************************************************************************


class GetFobiFormHandlerPluginCustomActionsNode(Node):
    """Node for ``get_fobi_form_handler_plugin_custom_actions`` tag."""

    def __init__(self, plugin, form_entry, as_var=None):
        """Constructor."""
        self.plugin = plugin
        self.form_entry = form_entry
        self.as_var = as_var

    def render(self, context):
        """Render."""
        request = context['request']
        plugin = self.plugin.resolve(context, True)
        form_entry = self.form_entry.resolve(context, True)

        context[self.as_var] = plugin.get_custom_actions(form_entry, request)
        return ''


@register.tag
def get_fobi_form_handler_plugin_custom_actions(parser, token):
    """Get the form handler plugin custom actions.

    Note, that ``plugin`` shall be a instance of
    ``fobi.models.FormHandlerEntry``.

    :syntax:

        {% get_fobi_form_handler_plugin_custom_actions
            [plugin] [form_entry] as [context_var_name] %}

    :example:

        {% get_fobi_form_handler_plugin_custom_actions
            plugin form_entry as form_handler_plugin_custom_actions %}
    """
    bits = token.contents.split()

    if len(bits) == 5:
        if bits[-2] != 'as':
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(
                    bits[0]
                )
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid "
            "syntax.".format(bits[0])
        )

    plugin = parser.compile_filter(bits[1])
    form_entry = parser.compile_filter(bits[2])

    return GetFobiFormHandlerPluginCustomActionsNode(
        plugin=plugin, form_entry=form_entry, as_var=as_var
    )

# *****************************************************************************
# ******************* Form wizard handler plugin specific *********************
# *****************************************************************************


class GetFobiFormWizardHandlerPluginCustomActionsNode(Node):
    """Node for ``get_fobi_form_wizard_handler_plugin_custom_actions`` tag."""

    def __init__(self, plugin, form_wizard_entry, as_var=None):
        """Constructor."""
        self.plugin = plugin
        self.form_wizard_entry = form_wizard_entry
        self.as_var = as_var

    def render(self, context):
        """Render."""
        request = context['request']
        plugin = self.plugin.resolve(context, True)
        form_wizard_entry = self.form_wizard_entry.resolve(context, True)

        context[self.as_var] = plugin.get_custom_actions(form_wizard_entry,
                                                         request)
        return ''


@register.tag
def get_fobi_form_wizard_handler_plugin_custom_actions(parser, token):
    """Get the form wizard handler plugin custom actions.

    Note, that ``plugin`` shall be a instance of
    ``fobi.models.FormWizardHandlerEntry``.

    :syntax:

        {% get_fobi_form_wizard_handler_plugin_custom_actions
            [plugin] [form_wizard_entry] as [context_var_name] %}

    :example:

        {% get_fobi_form_wizard_handler_plugin_custom_actions
            plugin form_wizard_entry as
                form_wizard_handler_plugin_custom_actions %}
    """
    bits = token.contents.split()

    if len(bits) == 5:
        if bits[-2] != 'as':
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(
                    bits[0]
                )
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid "
            "syntax.".format(bits[0])
        )

    plugin = parser.compile_filter(bits[1])
    form_wizard_entry = parser.compile_filter(bits[2])

    return GetFobiFormWizardHandlerPluginCustomActionsNode(
        plugin=plugin, form_wizard_entry=form_wizard_entry, as_var=as_var
    )

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** Additional Fobi tags ***************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


def render_auth_link(context):
    """Render auth link."""
    if not DISPLAY_AUTH_LINK:
        return {}

    request = context.get('request', None)
    user_is_authenticated = request.user.is_authenticated

    if request and user_is_authenticated:
        try:
            auth_url = settings.LOGOUT_URL
            auth_icon_class = 'icon-signout'
            auth_link_text = _('Log out')
        except Exception:
            auth_url = ''
            auth_icon_class = ''
            auth_link_text = ''
    else:
        try:
            auth_url = settings.LOGIN_URL
            auth_icon_class = 'icon-signin'
            auth_link_text = _('Log in')
        except Exception:
            auth_url = ''
            auth_icon_class = ''
            auth_link_text = ''

    return {
        'auth_link': auth_url,
        'auth_icon_class': auth_icon_class,
        'auth_link_text': auth_link_text
    }


register.inclusion_tag(
    'fobi/snippets/render_auth_link.html', takes_context=True
)(render_auth_link)


@register.inclusion_tag(THEME.forms_list_template, takes_context=True)
def render_fobi_forms_list(context, queryset, *args, **kwargs):
    """Render the list of fobi forms.

    :syntax:

        {% render_fobi_forms_list [queryset] [show_edit_link] \
                                             [show_delete_link] \
                                             [show_export_link] %}

    :example:

        {% render_fobi_forms_list queryset show_edit_link=True \
                                           show_delete_link=False \
                                           show_export_link=False %}
    """
    request = context.get('request', None)
    show_edit_link = kwargs.get('edit_link', False)
    show_delete_link = kwargs.get('delete_link', False)
    show_export_link = kwargs.get('export_link', False)
    return {
        'show_custom_actions': (
            show_edit_link or show_delete_link or show_export_link
        ),
        'show_edit_link': show_edit_link,
        'show_delete_link': show_delete_link,
        'show_export_link': show_export_link,
    }


# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** Permission tags ********************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


class HasEditFormEntryPermissionsNode(Node):
    """Node for ``has_edit_form_entry_permissions`` tag."""

    def __init__(self, as_var=None):
        """Constructor."""
        self.as_var = as_var

    def render(self, context):
        """Render."""
        try:
            perms = context['perms']
        except Exception as err:
            if self.as_var:
                context[self.as_var] = False
                return ''
            else:
                return False

        perms_required = [
            'fobi.add_formentry',
            'fobi.change_formentry',
            'fobi.delete_formentry',

            'fobi.add_formelemententry',
            'fobi.change_formelemententry',
            'fobi.delete_formelemententry',

            'fobi.add_formhandlerentry',
            'fobi.change_formhandlerentry',
            'fobi.delete_formhandlerentry',
        ]

        for perm in perms_required:
            if perm in perms:
                if self.as_var:
                    context[self.as_var] = True
                    return ''
                else:
                    return True

        if self.as_var:
            context[self.as_var] = False
            return ''
        else:
            return False


@register.tag
def has_edit_form_entry_permissions(parser, token):
    """Checks the permissions

    :syntax:

        {% has_edit_form_entry_permissions as [var_name] %}

    :example:

        {% has_edit_form_entry_permissions %}

        or

        {% has_edit_form_entry_permissions as has_permissions %}
    """
    bits = token.contents.split()

    if len(bits) not in (1, 3):
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. Incorrect number of arguments.".format(
                bits[0]
            )
        )

    if 3 == len(bits):
        as_var = bits[-1]

    else:
        as_var = None

    return HasEditFormEntryPermissionsNode(as_var=as_var)

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** General Django tags ****************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


class FormFieldType(object):
    """Form field type container."""

    is_checkbox = False
    is_password = False
    is_hidden = False
    is_text = False
    is_radio = False
    is_textarea = False

    def __init__(self, properties=[]):
        """Constructor.

        By default all of them are false. Provide only property
        names that should be set to True.
        """
        for prop in properties:
            setattr(self, prop, True)


class GetFormFieldTypeNode(Node):
    """Node for ``get_form_field_type`` tag."""

    def __init__(self, field, as_var=None):
        """Constructor."""
        self.field = field
        self.as_var = as_var

    def render(self, context):
        """Render."""
        field = self.field.resolve(context, True)
        properties = []

        if isinstance(field.field.widget, forms.CheckboxInput):
            properties.append('is_checkbox')

        if isinstance(field.field.widget, forms.CheckboxSelectMultiple):
            properties.append('is_checkbox_multiple')

        if isinstance(field.field.widget, forms.RadioSelect):
            properties.append('is_radio')

        res = FormFieldType(properties)

        context[self.as_var] = res
        return ''


@register.tag
def get_form_field_type(parser, token):
    """Get form field type.

    Syntax::

        {% get_form_field_type [field] as [context_var_name] %}

    Example::

        {% get_form_field_type form.field as form_field_type %}
        {% if form_field_type.is_checkbox %}
            ...
        {% endif %}
    """
    bits = token.contents.split()

    if len(bits) == 4:
        if bits[-2] != 'as':
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(
                    bits[0]
                )
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid "
            "syntax.".format(bits[0])
        )

    field = parser.compile_filter(bits[1])

    return GetFormFieldTypeNode(field=field, as_var=as_var)


class GetFormHiddenFieldsErrorsNode(Node):
    """Node for ``get_form_hidden_fields_errors`` tag."""

    def __init__(self, form, as_var=None):
        """Constructor."""
        self.form = form
        self.as_var = as_var

    def render(self, context):
        """Render."""
        form = self.form.resolve(context, True)

        hidden_fields_errors = ErrorDict()

        for field in form.hidden_fields():
            if field.errors:
                hidden_fields_errors.update({field.name: field.errors})

        context[self.as_var] = hidden_fields_errors
        return ''


@register.tag
def get_form_hidden_fields_errors(parser, token):
    """Get form hidden fields errors.

    :syntax:

        {% get_form_hidden_fields_errors [form] as [context_var_name] %}

    :example:

        {% get_form_hidden_fields_errors form as form_hidden_fields_errors %}
        {{ form_hidden_fields_errors.as_ul }}
    """
    bits = token.contents.split()

    if len(bits) == 4:
        if bits[-2] != 'as':
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(
                    bits[0]
                )
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid "
            "syntax.".format(bits[0])
        )

    form = parser.compile_filter(bits[1])

    return GetFormHiddenFieldsErrorsNode(form=form, as_var=as_var)
