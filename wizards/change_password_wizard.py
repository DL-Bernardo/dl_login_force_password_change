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
        self.env.user.write(
            {"password": self.password_new, "must_change_password": False}
        )
        return {
            "type": "ir.actions.act_url",
            "url": "/web",
            "target": "self",
        }
