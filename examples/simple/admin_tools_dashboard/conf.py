# *******************************
# ************ Foo **************
# *******************************
foo_apps = [
    'foo.models.*',
    'bar.models.*',
]

# *******************************
# ************ Fobi *************
# *******************************
fobi_plugins = [
    'fobi.models.FormElement',
    'fobi.models.FormHandler'
]

fobi_forms = [
    'fobi.models.FormWizardEntry',
    'fobi.models.FormEntry',
    'fobi.models.FormElementEntry',
    'fobi.models.FormFieldsetEntry',
    'fobi.models.FormHandlerEntry',
]

fobi_data = [
    'fobi.contrib.plugins.form_handlers.db_store.models.*',
]

feincms_pages = [
    'page.*',
]

djangocms_pages = [
    'cms.models.*',
]

# *******************************
# ************ Django ***********
# *******************************
django_contrib_apps = [
    'django.contrib.*',
]
other_apps = foo_apps
