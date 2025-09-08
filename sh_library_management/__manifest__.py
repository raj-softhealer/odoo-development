{
    'name': 'Library Management Task',
    'version': '1.0',
    'summary': 'Manage books, members, and borrowings in a library',
    'depends': ['base','mail','contacts'],
    "sequence":"1",
    "category":"Library",
    'data': [
        'security/ir.model.access.csv',
        'views/author_details_view.xml',
        'views/book_inventory_view.xml',
        'views/library_members_view.xml',
        'views/book_borrow.xml',
        'views/book_return_model.xml',
        'views/menu_items.xml',
        
    ],
    'application': True,
    'installable': True,
    
    }
