# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.
from odoo import fields,models,api

class NameSearchMethod(models.Model):
    _inherit = "res.users"

    def name_get(self):
        result=[]

        for rec in self:
            name = f"{rec.name} ({rec.login})"

            result.append((rec.id,name))

        return result


    @api.model
    def name_search(self, name='', args=None, operator='ilike',limit=100):
        if name:
            domain = ['|',('name',operator,name),('login',operator,name)]
        else:
            domain = args

        return self.search(domain,limit=limit).name_get()