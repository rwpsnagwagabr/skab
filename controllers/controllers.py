# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSecurityRwpst(http.Controller):
#     @http.route('/custom_security_rwpst/custom_security_rwpst', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_security_rwpst/custom_security_rwpst/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_security_rwpst.listing', {
#             'root': '/custom_security_rwpst/custom_security_rwpst',
#             'objects': http.request.env['custom_security_rwpst.custom_security_rwpst'].search([]),
#         })

#     @http.route('/custom_security_rwpst/custom_security_rwpst/objects/<model("custom_security_rwpst.custom_security_rwpst"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_security_rwpst.object', {
#             'object': obj
#         })

