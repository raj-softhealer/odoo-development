from odoo import fields,models


class ListItem(models.Model):
    _name="sale.custom.items"
    _description="Sale Custom Items"


    item_names=fields.Many2one("sale.order", string="Quotation Id")
    product_type = fields.Char(string="Product")
    product_quantity=fields.Float(string="Quantity")
    product_size=fields.Char(string="Size")