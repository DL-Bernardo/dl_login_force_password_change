# -*- coding: utf-8 -*-
# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# Copyright 2024-2026 DIGITALUB ANGOLA, LDA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ChangePasswordWizard(models.TransientModel):
    _name = "dl.change.password.wizard"
    _description = "Force Change Password Wizard"

    user_ids = fields.Many2many("res.users", string="Users")
    password_new = fields.Char(string="New Password", required=True)
    password_confirm = fields.Char(string="Confirm Password", required=True)

    def change_password(self):
        self.ensure_one()
        if self.password_new != self.password_confirm:
            raise UserError(_("New passwords do not match."))
        if len(self.password_new) < 8:
            raise UserError(_("The password must be at least 8 characters long."))
        self.env.user.write(
            {
                "password": self.password_new,
                "must_change_password": False,
                "password_last_changed": fields.Datetime.now(),
            }
        )
        return {
            "type": "ir.actions.act_url",
            "url": "/web",
            "target": "self",
        }