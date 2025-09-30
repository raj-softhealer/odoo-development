{
    'name': 'Alternative Products Management',
    'version': '1.0',
    'summary': 'To manage alternative products ',
    'depends': ['base','mail','sale_management'],
    "sequence":"1",
    "category":"sale",
    'data': [
        'security/ir.model.access.csv',
        'security/sh_alternate_product_security_groups.xml',
        'views/sh_alternative_product_view.xml',
        'views/sh_sale_orderline_button.xml',
        'wizard/sh_add_alternate_prouct_wizard_view.xml',           
        'wizard/sh_stock_view_wizard_view.xml',           
    ],
    'application': True,
    'installable': True,
    
    }
