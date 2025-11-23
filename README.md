# DL Force Password Change on First Login

## Summary

Este módulo força os utilizadores a alterar a sua palavra-passe na primeira vez que iniciam sessão no Odoo.

## Features

- Adiciona um campo "Must change password" ao modelo de utilizador.
- Se este campo estiver marcado, o utilizador é obrigado a alterar a sua palavra-passe no próximo início de sessão.
- Garante que a nova palavra-passe cumpre as políticas de segurança definidas.
- Os administradores podem redefinir a palavra-passe de um utilizador e forçar a alteração na próxima sessão.

## Installation

Para instalar este módulo, siga os seguintes passos:

1. Copie a pasta do módulo para o seu diretório de addons do Odoo.
2. Reinicie o serviço do Odoo.
3. Aceda ao menu "Apps" no Odoo.
4. Clique em "Update Apps List".
5. Procure por "DL Force Password Change on First Login" e clique em "Install".

## Usage

Para utilizar este módulo, siga os seguintes passos:

1. Aceda a "Settings" > "Users & Companies" > "Users".
2. Crie um novo utilizador ou selecione um existente.
3. Marque a caixa de verificação "Must change password".
4. Da próxima vez que o utilizador iniciar sessão, ser-lhe-á pedido que altere a sua palavra-passe.

## Author

DIGITALUB ANGOLA

## License

AGPL-3
