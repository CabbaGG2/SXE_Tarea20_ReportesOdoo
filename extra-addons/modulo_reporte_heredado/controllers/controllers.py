# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloReporteHeredado(http.Controller):
#     @http.route('/modulo_reporte_heredado/modulo_reporte_heredado', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_reporte_heredado/modulo_reporte_heredado/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_reporte_heredado.listing', {
#             'root': '/modulo_reporte_heredado/modulo_reporte_heredado',
#             'objects': http.request.env['modulo_reporte_heredado.modulo_reporte_heredado'].search([]),
#         })

#     @http.route('/modulo_reporte_heredado/modulo_reporte_heredado/objects/<model("modulo_reporte_heredado.modulo_reporte_heredado"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_reporte_heredado.object', {
#             'object': obj
#         })

