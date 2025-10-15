# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.
from odoo import fields,models,api

class TotalQuantityField(models.Model):
    _inherit = "sale.order"


    sh_total_quantity=fields.Integer(compute="_total_quantity_calc")



    @api.depends('order_line')
    def _total_quantity_calc(self):
        for rec in self:
            rec.sh_total_quantity = sum(rec.order_line.mapped('product_uom_qty'))
            



    def action_send_email_corn(self):
        '''This method will run every day to send today's sale orders of all selected companies'''
        
        company_id=self.env["res.company"].browse(self.env.context.get("allowed_company_ids"))

        for company in company_id:
            if company.sh_send_email:
                
                context = {
                        "current_company" : company.id,
                    }
                
                email_data={
                    'email_to' : ','.join(company.sh_user_to_send.mapped('login')),

                }
                
                mail_template=self.env.ref("sh_email_configuration.cron_job_mail_template")
                mail_template.with_context(context).send_mail(company.id,force_send=True,email_values=email_data)
        
