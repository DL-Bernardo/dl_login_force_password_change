{
    "name": "DL Force Password Change on First Login",
    "summary": "Forces users to change their password upon their first login.",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "website": "https://www.digitalub.ao",
    "author": "DIGITALUB ANGOLA",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base", "auth_password_policy"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_users_view.xml",
        "wizards/change_password_wizard_view.xml",
    ],
}
