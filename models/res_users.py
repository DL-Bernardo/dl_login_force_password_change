# Copyright 2016-2018 Tecnativa - Pedro M. Baeza
# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    must_change_password = fields.Boolean(
        string="Must change password",
        default=False,
        help="If checked, this user will be forced to change his/her password "
        "at next login.",
    )

    def write(self, vals):
        return super().write(vals)

    def action_reset_password(self):
        self.ensure_one()
        self.must_change_password = True
