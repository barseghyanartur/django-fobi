# *******************************
# ************ Foo **************
# *******************************
foo_apps = [
    'foo.models.*',
]

# *******************************
# ************ Fobi *************
# *******************************
fobi_plugins = [
    'fobi.models.FormElement', 'fobi.models.FormHandler'
]

fobi_forms = [
    'fobi.models.FormWizardEntry', 'fobi.models.FormEntry', 'fobi.models.FormElementEntry',
    'fobi.models.FormFieldsetEntry', 'fobi.models.FormHandlerEntry',
]

fobi_data = [
    'fobi.contrib.plugins.form_handlers.db_store.models.*',
]

feincms_pages = [
    'page.*',
]
# *******************************
# ************ Django ***********
# *******************************
apps_to_exclude = ['django.contrib.*',]
apps_to_exclude += foo_apps + fobi_plugins + fobi_forms + fobi_data + feincms_pages
