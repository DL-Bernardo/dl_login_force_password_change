# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ChangePasswordWizard(models.TransientModel):
    _name = "dl.change.password.wizard"
    _description = "Change Password Wizard"

    user_ids = fields.Many2many("res.users", string="Users")
    password_new = fields.Char(string="New Password", required=True)
    password_confirm = fields.Char(string="Confirm Password", required=True)

    def change_password(self):
        self.ensure_one()
        if self.password_new != self.password_confirm:
            raise UserError(_("New passwords do not match."))
        # self.env.user._check_password_policy(self.password_new)
        self.env.user.password = self.password_new
        self.env.user.must_change_password = False
        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
