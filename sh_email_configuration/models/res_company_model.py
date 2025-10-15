# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.
from odoo import fields,models


class StoreData(models.Model):
    _inherit ="res.company"


    sh_send_email=fields.Boolean()
    sh_user_to_send=fields.Many2many(comodel_name="res.users",relation="config_user_rel_stored",column1="config_col",column2="user_col")
    


    