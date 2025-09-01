from odoo import models,fields


class Designation(models.Model):
    _inherit="res.partner"


    des=fields.Many2many('res.users',string="Designation")  