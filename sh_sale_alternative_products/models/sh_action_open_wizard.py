from odoo import fields,models


class AlternateProductSale(models.Model):
    _inherit="sale.order.line"


    def open_alternate_prod_wizard(self):
        return{
            'name':'Alternate products',
            'type':'ir.actions.act_window',
            'res_model':'product.change',
            'view_mode': 'form',
            'target' : 'new',
        }