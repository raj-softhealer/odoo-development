# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.


from odoo import fields,models,api
from datetime import date,datetime,timedelta
from odoo.tools import date_utils


class SaleOrderHistory(models.Model):
    _inherit="sale.order"

    sh_order_history=fields.One2many("sale.order","partner_id",compute="_get_current_partner_orders")
    sh_reorder_val=fields.Boolean(related="company_id.sh_reorder")


    @api.depends("partner_id")
    def _get_current_partner_orders(self):
        '''
        This method will get the data of inserted in sale configuration and based on that
        it will search all sale orders 
        '''
        for rec in self:  

            # date_days= date_utils.subtract(date.today(),days=rec.company_id.sh_num_of_days)
            if rec.company_id.sh_num_of_days <= 0:
                date_days= date.today()
            else:
                date_days= date.today() - timedelta(days=rec.company_id.sh_num_of_days)


            sale_order_data=self.search([
                ('partner_id','=',rec.partner_id.id),
                ('id','!=',rec.id),
                # ('company_id','=',rec.company_id.id),
                ('date_order','>=',date_days),
                ('state','in',rec.company_id.sh_order_satges.mapped("sh_states")),
                ],limit=rec.company_id.sh_num_of_orders if rec.company_id.sh_num_of_orders > 0 else "0")
            
            rec.sh_order_history=sale_order_data


    def action_re_order_all(self):
        '''
        This method will take all products from all sale orders present in order history
        and re order all items in current sale order
        '''
        for records in self.sh_order_history:
            for order_lines in records.order_line:
                      
                self.order_line = [(0,0,{
                    'product_id' : order_lines.product_id.id,
                    'product_uom_qty': order_lines.product_uom_qty,
                    'price_unit' : order_lines.price_unit,
                })]

        
    def action_re_order(self):
        '''
        This method will re order from current clicked sale order
        '''
        sale_orer_line_data=self.env["sale.order"].browse(self.env.context["current__order_id"])

        for i in self.order_line:
            sale_orer_line_data.order_line = [(0,0,{
                'product_id' : i.product_id.id,
                'product_uom_qty': i.product_uom_qty,
                'price_unit' : i.price_unit,
            })]
    

    def action_view_order(self):
        '''
        This method will redirect to clicked order
        '''
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': self.id,
            'view_mode':'form'
        }
        


            
