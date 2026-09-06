{
    "name": "DL Force Password Change on First Login",
    "summary": "Force users to change their password upon their first login or on next login.",
    "version": "17.0.2.0.1",
    "category": "Authentication",
    "website": "https://www.digitalub.ao",
    "author": "DIGITALUB ANGOLA, LDA",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_users_view.xml",
        "wizards/change_password_wizard_view.xml",
    ],
    "images": [
        "static/description/banner.png",
        "static/description/screenshot1.png",
        "static/description/screenshot2.png",
        "static/description/screenshot3.png",
    ],
    "description": """
DL Force Password Change on First Login
=======================================
Security module that enforces users to change their password when they log in for the first time or when flagged by an administrator.

Key Features:
-------------
* Enforce password change at first login or next login.
* Works seamlessly for both newly created users and existing users.
* Clean and responsive modal wizard for password update.
* Tracks the last password change date.
* 100% Free Community Edition by DIGITALUB ANGOLA.

How to use:
-----------
1. Navigate to Settings > Users & Companies > Users.
2. Open a user profile.
3. Check the "Force Password Change on Next Login" option (or click "Force Now").
4. Upon the user's next login, they will be automatically prompted to set a new password.
    """,
}

