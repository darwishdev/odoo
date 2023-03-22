# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class retail_deps(models.Model):
#     _name = 'retail_deps.retail_deps'
#     _description = 'retail_deps.retail_deps'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
