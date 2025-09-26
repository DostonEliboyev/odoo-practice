# -*- coding: utf-8 -*-
# from odoo import http


# class Uicecommerce(http.Controller):
#     @http.route('/uicecommerce/uicecommerce', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uicecommerce/uicecommerce/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uicecommerce.listing', {
#             'root': '/uicecommerce/uicecommerce',
#             'objects': http.request.env['uicecommerce.uicecommerce'].search([]),
#         })

#     @http.route('/uicecommerce/uicecommerce/objects/<model("uicecommerce.uicecommerce"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uicecommerce.object', {
#             'object': obj
#         })

