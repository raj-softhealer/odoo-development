# -*- coding: utf-8 -*-

from odoo import fields,models,api

class AlternativePeoducts(models.Model):
    _inherit="product.product"


    sh_alt_products_ids = fields.Many2many("product.product",
                                  "product_to_product_rel",
                                  "current_product_ids",
                                  "prodcuts_product_ids",
                                  string="Select Alternate Products",
                                  domain="[('id','!=',id)]")
    

    def write(self,vals):
         
         '''
         This method will interconnect all record items on adding in field 
         'sh_alt_products_ids' and  while remove record item it will remove current 
         record from opposite side too  
         '''

         for rec in self:

            old_prodct_data=rec.sh_alt_products_ids

            res=super().write(vals)
            
            temp_data=rec.sh_alt_products_ids.ids
            temp_data.append(rec.id)

            for prod in rec.sh_alt_products_ids:
                for t in temp_data:
                    if  t != prod.id and t not in prod.sh_alt_products_ids.ids:
                            prod.write({'sh_alt_products_ids':[(4,t)]})

            # unlink from alternate from if removed from self
            new_prodct_data=rec.sh_alt_products_ids

            for old in old_prodct_data:
                if old not in new_prodct_data:
                    old.write({'sh_alt_products_ids': [(3,rec.id)]})
                                            
            return res   
    

    def action_open_view_stock_alternate_product(self):
        '''Will open the stock view wizard on click on "view stock" in 
        sale.order.line > open_alternate_prod_wizard (button) > sh_alternate_product_ids > view stock'''
        return {
            'name': f"{self.name} stock",
            'type' : 'ir.actions.act_window',
            'res_model': 'stock.view.wizard',
            'view_mode':'form',
            'target': 'new',
        }
