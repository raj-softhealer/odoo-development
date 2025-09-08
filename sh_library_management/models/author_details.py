from odoo import fields,models,api



class AuthorDetails(models.Model):
    _inherit="res.partner"


    # book_details=fields.One2many("book.inventory","author")
    book_count=fields.Integer(string="Books Written", compute="_compute_books_written")
    publisher_books=fields.Integer(string="Books Published", compute="_compute_books_published")
    is_active=fields.Boolean(default=True)



    def action_view_books(self):
        # self.ensure_one()

        return{
            'type':'ir.actions.act_window',
            'name' : f"Books of author {self.name}",
            'res_model': 'book.inventory',
            'view_mode': "list,form",
            'target':'current',
            'domain' : [('author','=',self.name)]
        }
    
    def action_view_published_book(self):
        self.ensure_one()
        return{
            'type':'ir.actions.act_window',
            'name':f'Published by {self.name}',
            'res_model' : 'book.inventory',
            'view_mode': 'list,form',
            'target': 'current',
            'domain' : [('publisher','=',self.name)]
        }
    

    def _compute_books_written(self):

        for rec in self:
            data=self.env["book.inventory"].search_count([('author.id','=',rec.id)])

            # print("-------------------",data)

            rec.book_count=data


    def _compute_books_published(self):
        for rec in self:
            data=self.env["book.inventory"].search_count([('publisher','=',rec.id)])
            
            rec.publisher_books=data


           


        
        
