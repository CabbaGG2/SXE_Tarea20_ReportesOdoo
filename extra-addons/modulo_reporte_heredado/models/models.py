# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulo_reporte_heredado(models.Model):
#     _name = 'modulo_reporte_heredado.modulo_reporte_heredado'
#     _description = 'modulo_reporte_heredado.modulo_reporte_heredado'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

