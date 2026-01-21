# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloReportes(http.Controller):
#     @http.route('/modulo_reportes/modulo_reportes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_reportes/modulo_reportes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_reportes.listing', {
#             'root': '/modulo_reportes/modulo_reportes',
#             'objects': http.request.env['modulo_reportes.modulo_reportes'].search([]),
#         })

#     @http.route('/modulo_reportes/modulo_reportes/objects/<model("modulo_reportes.modulo_reportes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_reportes.object', {
#             'object': obj
#         })

