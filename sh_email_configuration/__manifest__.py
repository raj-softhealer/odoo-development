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
        # 'views/sh_quantity_field_sale_order_view.xml',
        'views/sh_configuration_settings_view.xml',
        'report/sh_inherit_field_template_view.xml',
        'report/sh_report_template.xml',
        'data/sh_custom_email_template_view.xml',
        'data/sh_send_email_cron.xml',
        'data/sh_send_email_template_view.xml',
    ],

    "application":True,
    "licence": "LGPl-3",


}