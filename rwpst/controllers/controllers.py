# -*- coding: utf-8 -*-
# from odoo import http


# class Rwpst(http.Controller):
#     @http.route('/rwpst/rwpst', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rwpst/rwpst/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rwpst.listing', {
#             'root': '/rwpst/rwpst',
#             'objects': http.request.env['rwpst.rwpst'].search([]),
#         })

#     @http.route('/rwpst/rwpst/objects/<model("rwpst.rwpst"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rwpst.object', {
#             'object': obj
#         })

