# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.
from odoo import fields,api,models


class CustomReportTemplate(models.AbstractModel):
    _name = "report.sh_email_configuration.report_template_for_cron"
    _description = "Email for Daily Summary Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        '''This method will get the all sale order of company and
           send as docs in report 
        '''
        
        docs=self.env["sale.order"].search([('date_order','>=',fields.Date.today()),('state','=','sale'),('company_id','=',self.env.context.get("current_company"))])
        
        return {
            'doc_ids' : docids,
            'doc_model' : self.env.context.get("active_model"),
            'docs' : docs,
            'data' : data,
        }
        