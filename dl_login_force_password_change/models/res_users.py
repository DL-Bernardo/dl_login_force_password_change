# -*- coding: utf-8 -*-
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# Copyright 2024-2026 DIGITALUB ANGOLA, LDA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    must_change_password = fields.Boolean(
        string="Must Change Password",
        default=False,
        help="If checked, this user will be forced to change their password at next login.",
    )
    password_last_changed = fields.Datetime(
        string="Password Last Changed",
        readonly=True,
        help="Date and time when the user's password was last changed.",
    )

    def write(self, vals):
        if "password" in vals and "password_last_changed" not in vals:
            vals["password_last_changed"] = fields.Datetime.now()
        return super().write(vals)

    def action_reset_password(self):
        """Action button to force user to change password on next login."""
        self.ensure_one()
        self.must_change_password = True

    @api.model
    def _cron_force_password_change(self):
        """Optional periodic cron to force password renewal (disabled by default)."""
        pass