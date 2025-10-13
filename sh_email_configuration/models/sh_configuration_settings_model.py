from odoo import fields,models,api


class SeetingConfiguration(models.TransientModel):
    _inherit = "res.config.settings"



    sh_send_email=fields.Boolean(related="company_id.sh_send_email",readonly=False,help="If its Active It will send all quotation order of today")
    sh_user_to_send=fields.Many2many(comodel_name="res.users",relation="config_user_rel",column1="config_col",column2="user_col",related="company_id.sh_user_to_send",readonly=False,help="The selected members will get email")
