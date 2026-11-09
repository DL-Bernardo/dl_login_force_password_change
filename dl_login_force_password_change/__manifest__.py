{
    "name": "Force Password Change on First Login",
    "summary": "Force users to change their password upon their first login or after configurable expiration policy",
    "version": "19.0.2.0.9",
    "category": "Authentication",
    "website": "https://www.digitalub.ao",
    "author": "DIGITALUB ANGOLA, LDA",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "price": 0.0,
    "currency": "USD",
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
        "static/description/screenshot4.png",
        "static/description/screenshot5.png",
        "static/description/screenshot6.png",
    ],
    "description": """
Force Password Change on First Login
====================================
Advanced security module that enforces users to change their password when they log in for the first time, when flagged by an administrator, or periodically (default 11-month policy).

Key Features:
-------------
* Enforce password change at first login or on demand.
* Automatic password expiration cron (default: 11 months).
* Modern glassmorphism security portal for password change.
* Integrated Odoo backend wizard with current password verification.
* Password complexity enforcement (minimum 8 characters, uppercase letter, number/symbol).
* Tracks last password change timestamp.
* 100% Free Community Edition by DIGITALUB ANGOLA (Odoo 16.0, 17.0, 18.0, 19.0 & 20.0).

Live Demos:
-----------
* Odoo 16.0: https://demo16.invoiceone.ao
* Odoo 17.0: https://demo17.invoiceone.ao
* Odoo 18.0: https://demo18.invoiceone.ao
* Odoo 19.0: https://demo19.invoiceone.ao
* Odoo 20.0: https://demo20.invoiceone.ao
    """,
}
