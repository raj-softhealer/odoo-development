# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.

from odoo import fields,models
import random


class SaleSatges(models.Model):
    _name="sale.order.stages"
    _description="Sale Stage"


    name = fields.Char()
    sh_states=fields.Selection([
        ('draft','Quotation'),
        ('sent','Quotation Sent'),
        ('sale','Sales Order'),
        ('cancel','Cancelled'),
    ])
    color = fields.Integer(default=lambda r: random.randint(1,11))
