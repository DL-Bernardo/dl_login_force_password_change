# -*- coding: utf-8 -*-
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# Copyright 2024-2026 DIGITALUB ANGOLA, LDA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import re
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ChangePasswordWizard(models.TransientModel):
    _name = "dl.change.password.wizard"
    _description = "Force Change Password Wizard"

    password_current = fields.Char(string="Current Password", required=True)
    password_new = fields.Char(string="New Password", required=True)
    password_confirm = fields.Char(string="Confirm New Password", required=True)

    def change_password(self):
        self.ensure_one()
        user = self.env.user

        # 1. Validate current password
        try:
            user._check_credentials(self.password_current, {"interactive": True})
        except Exception:
            return self._show_warning(_("Current password is incorrect."))

        # 2. Validate new differs from current
        if self.password_new == self.password_current:
            return self._show_warning(_("The new password cannot be the same as the current password."))

        # 3. Validate confirmation
        if self.password_new != self.password_confirm:
            return self._show_warning(_("New passwords do not match."))

        # 4. Validate complexity
        if len(self.password_new) < 8:
            return self._show_warning(_("The password must be at least 8 characters long."))
        if not re.search(r"[A-Z]", self.password_new):
            return self._show_warning(_("The password must contain at least one uppercase letter."))
        if not re.search(r"[0-9!@#$%^&*(),.?\":{}|<>]", self.password_new):
            return self._show_warning(_("The password must contain at least one number or special character."))

        # 5. Save change
        user.write({
            "password": self.password_new,
            "must_change_password": False,
            "password_last_changed": fields.Datetime.now(),
        })

        return {
            "type": "ir.actions.act_url",
            "url": "/web",
            "target": "self",
        }

    def _show_warning(self, message):
        """Returns a user-friendly notification."""
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Security Notice"),
                "message": message,
                "sticky": False,
                "type": "danger",
            },
        }
