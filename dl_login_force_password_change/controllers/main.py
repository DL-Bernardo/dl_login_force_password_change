# -*- coding: utf-8 -*-
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# Copyright 2024-2026 DIGITALUB ANGOLA, LDA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import re
from odoo import http, fields, _
from odoo.http import request
from odoo.addons.web.controllers.home import Home as WebHome


class Home(WebHome):
    @http.route("/web/login", type="http", auth="public")
    def web_login(self, redirect=None, **kw):
        response = super().web_login(redirect=redirect, **kw)
        if request.session.uid and request.env.user.must_change_password and not request.env.user.share:
            return request.redirect("/dl_force_password_change/change_password")
        return response

    @http.route("/dl_force_password_change/change_password", type="http", auth="user", methods=["GET", "POST"])
    def change_password_page(self, **kw):
        user = request.env.user

        # If user does not need to change password, redirect to home
        if not user.must_change_password or user.share:
            return request.redirect("/web")

        error = None
        if request.httprequest.method == "POST":
            password_current = kw.get("password_current")
            password_new = kw.get("password_new")
            password_confirm = kw.get("password_confirm")

            try:
                # 1. Validate current password
                try:
                    user._check_credentials(password_current, {"interactive": True})
                except Exception:
                    raise ValueError(_("Current password is incorrect."))

                # 2. Validate new differs from current
                if password_new == password_current:
                    raise ValueError(_("The new password cannot be the same as the current password."))

                # 3. Validate confirmation
                if password_new != password_confirm:
                    raise ValueError(_("New passwords do not match."))

                # 4. Validate complexity
                if len(password_new) < 8:
                    raise ValueError(_("The password must be at least 8 characters long."))
                if not re.search(r"[A-Z]", password_new):
                    raise ValueError(_("The password must contain at least one uppercase letter."))
                if not re.search(r"[0-9!@#$%^&*(),.?\":{}|<>]", password_new):
                    raise ValueError(_("The password must contain at least one number or special character."))

                # 5. Save change
                user.write({
                    "password": password_new,
                    "must_change_password": False,
                    "password_last_changed": fields.Datetime.now(),
                })

                return request.redirect("/web")

            except ValueError as e:
                error = str(e)
            except Exception:
                error = _("An unexpected error occurred. Please try again.")

        return request.render("dl_login_force_password_change.change_password_layout", {
            "error": error
        })
