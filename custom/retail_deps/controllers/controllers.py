# -*- coding: utf-8 -*-
# from odoo import http


# class RetailDeps(http.Controller):
#     @http.route('/retail_deps/retail_deps', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/retail_deps/retail_deps/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('retail_deps.listing', {
#             'root': '/retail_deps/retail_deps',
#             'objects': http.request.env['retail_deps.retail_deps'].search([]),
#         })

#     @http.route('/retail_deps/retail_deps/objects/<model("retail_deps.retail_deps"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('retail_deps.object', {
#             'object': obj
#         })
