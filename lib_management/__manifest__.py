{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books, members, and borrowings in a library',
    'depends': ['base','mail','contacts','sale'],
    "sequence":"2",
    "category":"Ab",
    'data': [
        'security/ir.model.access.csv',
        # 'views/contact_extraa_views.xml',
        'views/category_views.xml',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/member_views.xml',
        'views/borrow_views.xml',
        'views/publisher_views.xml',
        # 'views/invoicing_extra_field_view.xml',
        'views/menu.xml',
    ],
    'application': True,
    'installable': True,
    
    }
