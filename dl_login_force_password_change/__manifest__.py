{
    "name": "DL Force Password Change on First Login",
    "summary": "Force users to change their password upon their first login or after 11 months.",
    "version": "17.0.2.0.2",
    "category": "Authentication",
    "website": "https://www.digitalub.ao",
    "author": "DIGITALUB ANGOLA, LDA",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_config_parameter.xml",
        "data/ir_cron.xml",
        "views/res_users_view.xml",
        "views/change_password_template.xml",
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
Advanced security module that enforces users to change their password when they log in for the first time, when flagged by an administrator, or periodically (default 11-month policy).

Key Features:
-------------
* Enforce password change at first login or on demand.
* Automatic password expiration cron (default: 11 months).
* Modern glassmorphism security portal for password change.
* Integrated Odoo backend wizard with current password verification.
* Password complexity enforcement (minimum 8 characters, uppercase letter, number/symbol).
* Tracks last password change timestamp.
* 100% Free Community Edition by DIGITALUB ANGOLA.

How to use:
-----------
1. Navigate to Settings > Users & Companies > Users.
2. Open a user profile.
3. Check the "Force Password Change on Next Login" option (or click "Force Now").
4. Newly created internal users are automatically prompted to set a new password on their first login.
    """,
}
