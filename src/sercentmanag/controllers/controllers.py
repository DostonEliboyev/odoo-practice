# -*- coding: utf-8 -*-
# from odoo import http


# class Sercentmanag(http.Controller):
#     @http.route('/sercentmanag/sercentmanag', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sercentmanag/sercentmanag/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sercentmanag.listing', {
#             'root': '/sercentmanag/sercentmanag',
#             'objects': http.request.env['sercentmanag.sercentmanag'].search([]),
#         })

#     @http.route('/sercentmanag/sercentmanag/objects/<model("sercentmanag.sercentmanag"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sercentmanag.object', {
#             'object': obj
#         })

