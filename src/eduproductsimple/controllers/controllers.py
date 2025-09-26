# -*- coding: utf-8 -*-
# from odoo import http


# class Eduproductsimple(http.Controller):
#     @http.route('/eduproductsimple/eduproductsimple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eduproductsimple/eduproductsimple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eduproductsimple.listing', {
#             'root': '/eduproductsimple/eduproductsimple',
#             'objects': http.request.env['eduproductsimple.eduproductsimple'].search([]),
#         })

#     @http.route('/eduproductsimple/eduproductsimple/objects/<model("eduproductsimple.eduproductsimple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eduproductsimple.object', {
#             'object': obj
#         })

