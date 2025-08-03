# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request


class Home(http.Controller):
    @http.route("/web/login", type="http", auth="none")
    def web_login(self, redirect=None, **kw):
        response = super(Home, self).web_login(redirect=redirect, **kw)
        if request.session.uid and request.env.user.must_change_password:
            return http.redirect_with_hash("/web/session/change_password")
        return response
