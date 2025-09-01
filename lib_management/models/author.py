from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Book Author'

    name = fields.Char(string="Author Name", required=True)
    biography = fields.Text(string="Biography")
    book_ids = fields.One2many('library.book', 'author_id', string="Books")




    