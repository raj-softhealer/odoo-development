from odoo import models,fields,api

class ProductDescription(models.Model):
    _inherit="sale.order"


    add_item=fields.One2many("sale.custom.items","item_names")



    def open_wizard_add_item(self):
        return {
            'type':'ir.actions.act_window',
            'res_model' : 'add.item.number',
            'view_mode' : 'form',
            'target' : 'new',
        }

    def open_wizard_add_item_using_six_zero(self):
        return {
            'type':'ir.actions.act_window',
            'res_model' : 'add.item.number.sixzero',
            'view_mode' : 'form',
            'target' : 'new',
        }