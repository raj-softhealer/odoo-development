from odoo import fields,models,api

class TotalQuantityField(models.Model):
    _inherit = "sale.order"


    sh_total_quantity=fields.Integer(compute="_total_quantity_calc")



    @api.depends('order_line')
    def _total_quantity_calc(self):
        for rec in self:
            rec.sh_total_quantity = sum(rec.order_line.mapped('product_uom_qty'))
            



    def action_send_email_corn(self):
        if self.env.company.sh_send_email:
            email_data={
                'email_to' :','.join(self.env.company.sh_user_to_send.mapped('login'))
            }
            
            mail_template=self.env.ref("sh_email_configuration.cron_job_mail_template")
            mail_template.send_mail(self.id,force_send=True,email_values=email_data)
        
