# -*- coding: utf-8 -*-
# from odoo import http


# class Writelogs(http.Controller):
#     @http.route('/writelogs/writelogs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/writelogs/writelogs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('writelogs.listing', {
#             'root': '/writelogs/writelogs',
#             'objects': http.request.env['writelogs.writelogs'].search([]),
#         })

#     @http.route('/writelogs/writelogs/objects/<model("writelogs.writelogs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('writelogs.object', {
#             'object': obj
#         })

