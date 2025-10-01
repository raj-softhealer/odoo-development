# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT. LTD.

from odoo import fields,models,api

class ViewStock(models.TransientModel):
    _name="stock.view.wizard"
    _description="View Stock"

    view_stock=fields.Many2many("stock.quant","view_stock_rel","col1","col2")


    @api.model
    def default_get(self,vals):
        '''
        will get value of current product and find that product in "stock.quant"
        model and show all the records
        '''

        res = super().default_get(vals)

        if self.env.context['active_model'] == 'product.change':
            print(f"\n\n\n\n default get occures {self.env.context}")
            prod=self.env["product.change"].browse(self.env.context.get('active_id'))

            warehouse_stock=self.env["stock.quant"].search([('product_id','=',prod.product_id.id),("location_id.usage", "=", "internal")])

            res["view_stock"]  = warehouse_stock


        elif self.env.context['active_model'] == 'product.product':
            print(f"\n\n\n\n default get occures {self.env.context}")

            warehouse_stock=self.env["stock.quant"].search([('product_id','=',self.env.context.get("active_id")),("location_id.usage", "=", "internal")])

            res["view_stock"] = warehouse_stock
    
        return res
    

    def action_go_back(self):
        '''
        on click on "go back" this method will call
        '''
        if self.env.context['active_model'] == 'product.change':
            return {
            'type' : 'ir.actions.act_window',
            'res_model': 'product.change',
            'res_id': self.env.context["wizard_id"],
            'view_mode':'form',
            'target': 'new',
            }
            
        elif self.env.context['active_model'] == 'product.product':
            return {
            'type' : 'ir.actions.act_window',
            'res_model': 'product.change',
            'res_id': self.env.context["wizard_id"],
            'view_mode':'form',
            'target': 'new',
            }

