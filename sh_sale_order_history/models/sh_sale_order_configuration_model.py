# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.

from odoo import fields,models,api


class CustomConfiguration(models.TransientModel):
    _inherit="res.config.settings"
    
    sh_num_of_orders = fields.Integer(related="company_id.sh_num_of_orders",readonly=False)
    sh_num_of_days = fields.Integer(related="company_id.sh_num_of_days",readonly=False)
    sh_order_satges = fields.Many2many("sale.order.stages","sale_order_stage_trnasient_rel","col1","col2",related="company_id.sh_order_satges",readonly=False)
    sh_reorder=fields.Boolean(related="company_id.sh_reorder",readonly=False)


    # @api.model
    # def default_get(self,vals):
    #     '''
    #     will get the values of stages in sale order and create with that value in
    #     model "sale.order.stages" if not in model
    #     '''
    #     res = super().default_get(vals)

    #     stage_m2m_data= self.env["sale.order.stages"].search([])
    #     temp_name_data = stage_m2m_data.mapped("name")

    #     satetes_data=self.env["sale.order"]._fields["state"].selection

    #     if len(temp_name_data) != len(satetes_data):

    #         for rec in satetes_data:
    #             if rec[1] not in temp_name_data:
    #                 stage_m2m_data.create({'name':rec[1]})

    #     return res

