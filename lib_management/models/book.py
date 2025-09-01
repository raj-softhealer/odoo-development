from odoo import models, fields,api
import random

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['mail.thread',
                'mail.activity.mixin'
               ]

    name = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN")
    author_id=fields.Many2one("library.author", string="Author")
    publisher_id=fields.Many2one("library.publisher",string="Publisher")
    # member_ids=fields.Many2many("library.member", string="Borrowed By")
    borrow_ids=fields.One2many("library.borrow","book_id", string="Borrow History")
    published_date = fields.Date(string="Published Date")
    book_category = fields.Many2many("library.category","category_book_rel","book_id","category_id", string="Category")
    warn=fields.Text(string="Warning")


    @api.onchange('name')
    def _random_isbn(self):
        print("method called--------------------------------")
        # if self.name:
        for records in self:
            if records.isbn == False and records.name:
                records.isbn=random.randint(1000000000000,9999999999999)

            print("name--------------------------",records.name)
            if (records.name == False):
                records.warn=""
            elif (len(records.name) > 10):
                records.warn="The Author field is empty please fill it first and save"


        

        

