from odoo import fields,models


class BookInventory(models.Model):
    _name="book.inventory"
    _description="Book Inventory"
    _rec_name="book_title"
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
        ('issued','Not Available')
    ], tracking=True)

    borrowed=fields.Many2many("book.borrow","book_and_borrow_rel","book_ids","borrower_ids", compute="_get_borrower_data")

    total_borrowed_history=fields.Many2many("book.borrow","book_and_borrow_history_rel","book_ids_history","borrower_ids_history", compute="_get_borrower_data_total_history")


    copies=fields.Integer()
    available_copies=fields.Integer(compute="_action_count_copies")



    def _get_borrower_data(self):
        for rec in self:
            data=self.env["book.borrow"].search([('book_id','=', self.id),('status','=','borrowed')])
            # print("borrower data--------------",data)
            if data:
                for i in range(len(data)):
                    # print("ddddddtatatata",data[i])
                    rec.borrowed= [(4,data[i].id)]
            else:
                    rec.borrowed= False


    def _get_borrower_data_total_history(self):
        for rec in self:
            data=self.env["book.borrow"].search([('book_id','=', self.id)])
            print("borrower data--------------",data)
            if data:
                for i in range(len(data)):
                    # print("ddddddtatatata",data[i])
                    rec.total_borrowed_history= [(4,data[i].id)]
            else:
                    rec.total_borrowed_history= False
                

    def action_copies(self):
        pass
        # self.ensure_one()

        # return {
        #     'type':'ir.actions.act_window',
        #     'name': "",
        #     'res_model' : 'book.inventory',
        #     'view_mode' : 'list,form',
        #     'target': 'current'
        # }
    
    def _action_count_copies(self):

        for rec in self:

            find_borrower=self.env["book.borrow"].search_count([('book_id','=', self.id),('status','=','borrowed')])
            
            rec.available_copies=self.copies - find_borrower

            if rec.available_copies <= 0:
                self.status = 'issued'
            else:
                self.status = 'available'

    
