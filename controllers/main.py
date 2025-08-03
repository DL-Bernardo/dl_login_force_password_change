# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home as WebHome


class Home(WebHome):
    @http.route("/web/login", type="http", auth="public")
    def web_login(self, redirect=None, **kw):
        response = super().web_login(redirect=redirect, **kw)
        if request.session.uid and request.env.user.must_change_password:
            return http.redirect("/dl_force_password_change/change_password")
        return response

    @http.route("/dl_force_password_change/change_password", type="http", auth="user")
    def change_password_redirect(self, **kw):
        action = (
            request.env["ir.actions.act_window"]
            .sudo()
            .search([("res_model", "=", "dl.change.password.wizard")], limit=1)
        )
        if not action:
            return request.redirect("/web")
        return request.redirect(f"/web#action={action.id}")
