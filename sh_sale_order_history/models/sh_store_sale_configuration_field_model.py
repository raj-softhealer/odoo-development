# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.


from odoo import fields,models

class StoreSaleField(models.Model):
    _inherit = "res.company"
    
    sh_num_of_orders = fields.Integer()
    sh_num_of_days = fields.Integer()
    sh_order_satges = fields.Many2many("sale.order.stages","sale_order_stage_rel","col1","col2")
    sh_reorder=fields.Boolean()