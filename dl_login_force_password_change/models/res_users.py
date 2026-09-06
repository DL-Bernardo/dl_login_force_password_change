# -*- coding: utf-8 -*-
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# Copyright 2024-2026 DIGITALUB ANGOLA, LDA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from dateutil.relativedelta import relativedelta


class ResUsers(models.Model):
    _inherit = "res.users"

    must_change_password = fields.Boolean(
        string="Must Change Password",
        default=False,
        help="If checked, this user will be forced to change their password at next login.",
    )

    password_last_changed = fields.Datetime(
        string="Password Last Changed",
        default=fields.Datetime.now,
        readonly=True,
        help="Date and time when the user's password was last changed.",
    )

    @api.model_create_multi
    def create(self, vals_list):
        users = super().create(vals_list)
        for user, vals in zip(users, vals_list):
            if "must_change_password" not in vals and not user.share:
                user.must_change_password = True
        return users

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
        """Periodic cron to expire passwords based on configured months."""
        expiration_months = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("dl_force_password_change.expiration_months", 11)
        )
        limit_date = fields.Datetime.now() - relativedelta(months=expiration_months)
        users_to_expire = self.search([
            ("must_change_password", "=", False),
            ("password_last_changed", "<", limit_date),
            ("share", "=", False),
        ])
        if users_to_expire:
            users_to_expire.write({"must_change_password": True})
