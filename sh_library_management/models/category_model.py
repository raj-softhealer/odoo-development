from odoo import fields,models


class Categories(models.Model):
    _name="book.categories"
    _description="Book Categories"

    name=fields.Char(string="Category")