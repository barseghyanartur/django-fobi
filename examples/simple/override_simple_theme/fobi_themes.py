from fobi.base import theme_registry

from fobi.contrib.themes.simple.fobi_themes import SimpleTheme

__all__ = ('MySimpleTheme',)


class MySimpleTheme(SimpleTheme):
    """Overriding the "simple" theme."""

    html_classes = ['my-simple-theme']
    base_view_template = 'override_simple_theme/base_view.html'
    form_ajax = 'override_simple_theme/snippets/form_ajax.html'
    form_snippet_template_name = \
        'override_simple_theme/snippets/form_snippet.html'


# It's important to set the `force` argument to True, in
# order to override the original theme. Force can be applied
# only once.
theme_registry.register(MySimpleTheme, force=True)
