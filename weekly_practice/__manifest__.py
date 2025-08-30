{
    'name': 'Weekly Practice',
    'version': '18.0.1.0.0',
    'summary': 'Odoo 18 weekly Practice',
    'author': 'Raj Muliya',
    'license': 'LGPL-3',
    'category': 'Wkkly Practice',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_description_view.xml',
        'views/item_list_view.xml',
        'views/add_items_view.xml',
        'views/add_items_number_wizard.xml',
        'views/add_items_number_sixzero_wizard.xml',
    ],
    'installable': True,
    'application': True,
}