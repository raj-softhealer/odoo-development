from odoo import models, fields

class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = 'Book Publisher'

    name = fields.Char(string="Publisher Name", required=True)
    website = fields.Char(string="Website")
    book_ids = fields.One2many('library.book', 'publisher_id', string="Published Books")
