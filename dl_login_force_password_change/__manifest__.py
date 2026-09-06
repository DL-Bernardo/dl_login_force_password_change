{
    "name": "DL Force Password Change on First Login",
    "summary": "Força os utilizadores a alterar a password no primeiro login.",
    "version": "17.0.1.0.1",
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
Módulo de segurança que obriga os utilizadores a alterar a senha
na primeira vez que fazem login.

Como funciona:
- Crie um novo utilizador (ou edite um existente);
- Ative a opção **Force password change on Next Login**;
- No próximo login, o utilizador será redirecionado para definir uma nova senha.

Benefícios:
- Melhoria da segurança no ambiente Odoo;
- Garante que novos utilizadores escolham uma senha pessoal;
- Fácil de configurar e utilizar.
    """,
}
