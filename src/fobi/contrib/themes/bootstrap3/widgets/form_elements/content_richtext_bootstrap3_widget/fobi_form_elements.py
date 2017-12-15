from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.content.content_richtext.widgets \
    import (
        BaseContentRichTextPluginWidget
    )
from fobi.contrib.themes.bootstrap3 import UID

__title__ = 'fobi.contrib.themes.bootstrap3.widgets.form_elements.' \
            'content_richtext_bootstrap3_widget.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentRichTextPluginWidget',)


class ContentRichTextPluginWidget(BaseContentRichTextPluginWidget):
    """ContentRichText plugin widget for Bootstrap 3."""

    theme_uid = UID
    media_js = [
        'ckeditor/ckeditor-init.js',
        'ckeditor/ckeditor/ckeditor.js',
        # 'bootstrap3/js/fobi.plugin.slider-bootstrap3-widget.js',
    ]
    # media_css = [
    #     'bootstrap3/css/bootstrap-slider.min.css',
    #     'bootstrap3/css/fobi.plugin.slider-bootstrap3-widget.css',
    # ]


# Registering the widget
form_element_plugin_widget_registry.register(ContentRichTextPluginWidget)
