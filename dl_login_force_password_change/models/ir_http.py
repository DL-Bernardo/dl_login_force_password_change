# -*- coding: utf-8 -*-
# Copyright 2024-2026 DIGITALUB ANGOLA, LDA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import logging
from odoo import models, http, _
from odoo.http import request
from odoo.exceptions import AccessError

_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _dispatch(cls, endpoint):
        # Only enforce if request session is authenticated and user needs to change password
        if request.session.uid:
            try:
                user = request.env["res.users"].sudo().browse(request.session.uid)
                if user and user.exists() and user.must_change_password and not user.share:
                    path = request.httprequest.path
                    allowed_paths = [
                        "/dl_force_password_change/change_password",
                        "/web/login",
                        "/web/logout",
                        "/web/session/logout",
                    ]

                    is_allowed = any(path == p for p in allowed_paths) or \
                                 path.startswith("/web/content/") or \
                                 path.startswith("/web/static/") or \
                                 path.startswith("/web/assets/") or \
                                 path.startswith("/web/image/")

                    if not is_allowed:
                        is_json = getattr(request, "dispatcher", None) and request.dispatcher.routing_type == "json"
                        if is_json:
                            raise AccessError(_("You must change your password to continue."))
                        else:
                            return request.redirect("/dl_force_password_change/change_password")
            except AccessError:
                raise
            except Exception as e:
                _logger.exception("DL_LOGIN_FORCE: Exception in _dispatch: %s", str(e))
        return super()._dispatch(endpoint)
