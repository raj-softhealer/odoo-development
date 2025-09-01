from odoo import fields,models,api



class AuthorDetails(models.Model):
    _inherit="res.partner"


    # book_details=fields.One2many("book.inventory","author")
    book_count=fields.Integer(string="Books Written", compute="_compute_books_written")



    def action_view_books(self):
        # self.ensure_one()

        return{
            'type':'ir.actions.act_window',
            'name' : "Books of author {self.name}",
            'res_model': 'book.inventory',
            'view_mode': "list,form",
            'target':'current',
            # 'domain' : [('author','=',self.name)]
        }
    

    def _compute_books_written(self):
        for rec in self:
            data=self.env["book.inventory"].search([('author','=',rec.name)])
            print(self.env.context)
            rec.book_count=1


           


        
        
