from odoo import fields,models

class AddExtrainOrder(models.Model):
    _inherit="sale.order"


    lmk=fields.Char(string="Customer Name(new)")
    