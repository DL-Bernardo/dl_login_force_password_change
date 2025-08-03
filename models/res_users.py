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

    @api.model
    def get_password_policy(self):
        params = self.env["ir.config_parameter"].sudo()
        return {
            "min_length": int(params.get_param("auth_password_policy.min_length", 8)),
            "history_length": int(params.get_param("auth_password_policy.history_length", 6)),
            "check_complexity": params.get_param("auth_password_policy.check_complexity", True),
        }

    def _check_password_policy(self, password):
        policy = self.get_password_policy()
        if not password or len(password) < policy["min_length"]:
            raise UserError(
                _("Password must be at least %d characters long.") % policy["min_length"]
            )
        if policy["check_complexity"]:
            if not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password):
                raise UserError(
                    _("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
                )

    def write(self, vals):
        # if "password" in vals:
        #     for user in self:
        #         self._check_password_policy(vals["password"])
        return super().write(vals)

    def action_reset_password(self):
        self.ensure_one()
        self.must_change_password = True
