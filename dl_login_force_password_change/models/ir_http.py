# -*- coding: utf-8 -*-
from odoo import models, http, _
from odoo.http import request
from odoo.exceptions import AccessError
import logging

_logger = logging.getLogger(__name__)

class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _dispatch(cls, endpoint):
        # Only enforce if request session is authenticated and user needs to change password
        if request.session.uid:
            try:
                # Use sudo().browse to get the correct user even on auth="none" routes (like /web)
                user = request.env['res.users'].sudo().browse(request.session.uid)
                if user and user.exists() and user.must_change_password and not user.share:
                    path = request.httprequest.path
                    allowed_paths = [
                        '/dl_force_password_change/change_password',
                        '/web/login',
                        '/web/logout',
                        '/web/session/logout',
                    ]
                    
                    is_allowed = any(path == p for p in allowed_paths) or \
                                 path.startswith('/web/content/') or \
                                 path.startswith('/web/static/') or \
                                 path.startswith('/web/assets/') or \
                                 path.startswith('/web/image/')
                    
                    _logger.info("DL_LOGIN_FORCE: Path %s, is_allowed=%s, must_change=True, share=False", path, is_allowed)
                    if not is_allowed:
                        is_json = getattr(request, 'dispatcher', None) and request.dispatcher.routing_type == 'json'
                        _logger.info("DL_LOGIN_FORCE: Path %s, is_allowed=%s, is_json=%s", path, is_allowed, is_json)
                        if is_json:
                            _logger.info("DL_LOGIN_FORCE: Raising AccessError for JSON request on path %s", path)
                            raise AccessError(_("You must change your password to continue."))
                        else:
                            _logger.info("DL_LOGIN_FORCE: Redirecting HTTP request for path %s to /dl_force_password_change/change_password", path)
                            return request.redirect('/dl_force_password_change/change_password')
            except AccessError:
                raise
            except Exception as e:
                _logger.exception("DL_LOGIN_FORCE: Exception in _dispatch: %s", str(e))
        return super()._dispatch(endpoint)
