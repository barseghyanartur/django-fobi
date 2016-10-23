from fobi.base import form_element_plugin_widget_registry

from sample_textarea.widgets import BaseSampleTextareaPluginWidget


class SampleTextareaPluginWidget(BaseSampleTextareaPluginWidget):
    """SampleTextareaPluginWidget."""

    theme_uid = 'sample_layout'  # Theme for which the widget is loaded
    media_js = [
        'sample_layout/js/fobi.plugins.form_elements.sample_textarea.js',
    ]
    media_css = [
        'sample_layout/css/fobi.plugins.form_elements.sample_textarea.css',
    ]


form_element_plugin_widget_registry.register(SampleTextareaPluginWidget)
