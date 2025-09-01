from odoo import fields,models


class BookInventory(models.Model):
    _name="book.inventory"
    _description="Book Inventory"
    _inherit = ['mail.thread',
                'mail.activity.mixin'
               ]



    book_title=fields.Char(string="Book Title", tracking=True)
    author=fields.Many2many("res.partner","book_author_rel","book_id","author_id",string="Author", tracking=True)
    categories=fields.Many2many("book.categories",string="Categories", tracking=True)
    publisher=fields.Many2one("res.partner",string="Publisher", tracking=True)
    isbn=fields.Integer(string="ISBN", tracking=True)


    currency_id = fields.Many2one('res.currency', string="Currency",
                                 default=lambda self: self.env.user.company_id.currency_id)
    
    price=fields.Monetary(string="Defined Price", currency_field="currency_id", tracking=True)


    status=fields.Selection([
        ('available','Available'),
        ('issued','Issued')
    ], tracking=True)



