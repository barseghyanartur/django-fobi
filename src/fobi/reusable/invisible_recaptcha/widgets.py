from django.forms.widgets import CheckboxInput
from django.utils.safestring import mark_safe

__title__ = 'fobi.reusablbe.invisible_recaptcha.widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvisibleRecaptchaWidget',)


class InvisibleRecaptchaWidget(CheckboxInput):
    """Invisible recaptcha widget."""

    class Media(object):
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')

    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs.update({'data-customforms': 'disabled'})
        kwargs.update({'attrs': attrs})
        super(InvisibleRecaptchaWidget, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        """
        Returns this Widget rendered as HTML, as a Unicode string.
        """
        html = super(InvisibleRecaptchaWidget, self).render(*args, **kwargs)
        invisible_recaptcha_html = """
            <script src="://www.google.com/recaptcha/api.js" async defer>
            </script>
            <script>
              function g_recaptcha_onSubmit(token) { 
                document.getElementById("fobi-form").submit(); 
              }
            </script>
        """
        return html + mark_safe(invisible_recaptcha_html)
