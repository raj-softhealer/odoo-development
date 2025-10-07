# -*- coding: utf-8 -*-
# Part of SoftHealer Technologies PVT.LTD.

{
    "name": "Sale Order History",
    "category":"Sales",
    "sequence": 1,
    "summary": "Show sale order history",
    "description": '''This module will show the history of 
    selected users previous orders''',

    "depends":["base","contacts","sale_management"],
    "data": [
        'security/ir.model.access.csv',
        'views/sh_sale_order_configuration_view.xml',
        'views/sh_sale_order_history_view.xml', 
        'data/sh_demo_data.xml',
    ],

    "application":True,
    "licence": "LGPl-3",


}