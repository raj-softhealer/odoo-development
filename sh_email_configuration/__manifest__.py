# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.

{
    "name": "Email Configuration",
    "category":"Email",
    "sequence": 1,
    "summary": "Practice for email server and etc",
    "description": '''This module is for practice to email configuration''',

    "depends":["base","contacts","sale_management"],
    "data": [
        'views/res_config_settings_view.xml',
        'report/sh_inherit_field_template_view.xml',
        'report/sale_order_templates.xml',
        'report/sale_order_reports.xml',
        'data/mail_data.xml',
        'data/ir_cron_sale_order_data.xml',
        # 'data/sh_send_email_template_view.xml',
    ],

    "application":True,
    "licence": "LGPl-3",


}