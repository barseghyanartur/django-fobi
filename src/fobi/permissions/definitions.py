__title__ = "fobi.permissions.definitions"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "dashboard_permissions",
    "wizards_dashboard_permissions",
    "create_form_entry_permissions",
    "edit_form_entry_permissions",
    "delete_form_entry_permissions",
    "add_form_element_entry_permission",
    "edit_form_element_entry_permission",
    "delete_form_element_entry_permission",
    "add_form_handler_entry_permission",
    "edit_form_handler_entry_permission",
    "delete_form_handler_entry_permission",
    "create_form_wizard_entry_permissions",
    "edit_form_wizard_entry_permissions",
    "delete_form_wizard_entry_permissions",
    "add_form_wizard_form_entry_permission",
    "delete_form_wizard_form_entry_permission",
    "add_form_wizard_handler_entry_permission",
    "edit_form_wizard_handler_entry_permission",
    "delete_form_wizard_handler_entry_permission",
)

# Used in `dashboard` view.
dashboard_permissions = [
    # Form
    "fobi.add_formentry",
    "fobi.change_formentry",
    "fobi.delete_formentry",
]

# Used in `form_wizards_dashboard` view.
wizards_dashboard_permissions = [
    # Form wizard
    "fobi.add_formwizardentry",
    "fobi.change_formwizardentry",
    "fobi.delete_formwizardentry",
]

# Used in `create_form_entry` view.
create_form_entry_permissions = [
    "fobi.add_formentry",
    "fobi.add_formelemententry",
    "fobi.add_formhandlerentry",
]

# Used in `edit_form_entry` view.
edit_form_entry_permissions = [
    "fobi.change_formentry",
    "fobi.change_formelemententry",
    "fobi.change_formhandlerentry",
    "fobi.add_formelemententry",
    "fobi.add_formhandlerentry",
    "fobi.delete_formelemententry",
    "fobi.delete_formhandlerentry",
]

# Used in `delete_form_entry` view.
delete_form_entry_permissions = [
    "fobi.delete_formentry",
    "fobi.delete_formelemententry",
    "fobi.delete_formhandlerentry",
]

# Used in `add_form_element_entry` view.
add_form_element_entry_permission = "fobi.add_formelemententry"

# Used in `edit_form_element_entry` view.
edit_form_element_entry_permission = "fobi.change_formelemententry"

# Used in `delete_form_element_entry` view.
delete_form_element_entry_permission = "fobi.delete_formelemententry"

# Used in `add_form_handler_entry` view.
add_form_handler_entry_permission = "fobi.add_formhandlerentry"

# Used in `edit_form_handler_entry` view.
edit_form_handler_entry_permission = "fobi.change_formhandlerentry"

# Used in `delete_form_handler_entry` view.
delete_form_handler_entry_permission = "fobi.delete_formhandlerentry"

# Used in `create_form_wizard_entry` view.
create_form_wizard_entry_permissions = [
    "fobi.add_formwizardentry",
    "fobi.add_formwizardformentry",
    "fobi.add_formhandlerentry",
]

# Used in `edit_form_wizard_entry` view.
edit_form_wizard_entry_permissions = [
    "fobi.change_formwizardentry",
    "fobi.add_formwizardformentry",
    "fobi.delete_formewizardformentry",
    "fobi.add_formhandlerentry",
    "fobi.change_formhandlerentry",
    "fobi.delete_formhandlerentry",
]

# Used in `delete_form_wizard_entry` view.
delete_form_wizard_entry_permissions = [
    "fobi.delete_formwizardentry",
    "fobi.delete_formwizardformentry",
    "fobi.delete_formwizardhandlerentry",
]

# Used in `add_form_wizard_form_entry` view.
add_form_wizard_form_entry_permission = "fobi.add_formwizardformentry"

# Used in `delete_form_wizard_form_entry` view.
delete_form_wizard_form_entry_permission = "fobi.delete_formwizardformentry"

# Used in `add_form_wizard_handler_entry` view.
add_form_wizard_handler_entry_permission = "fobi.add_formwizardhandlerentry"

# Used in `edit_form_wizard_handler_entry` view.
edit_form_wizard_handler_entry_permission = "fobi.change_formwizardhandlerentry"

# Used in `delete_form_wizard_handler_entry` view.
delete_form_wizard_handler_entry_permission = (
    "fobi.delete_formwizardhandlerentry"
)
