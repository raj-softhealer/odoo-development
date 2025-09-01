from odoo import fields,models

class Category(models.Model):
    _name="library.category"
    _description="Library Category"

    name=fields.Char(string="Category",required=True,)