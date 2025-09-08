from odoo import fields,models,api
from datetime import datetime,timedelta
from odoo.exceptions import UserError

class BorrowBook(models.Model):
    _name="book.borrow"
    _rec_name="borrower_id"
    _description="Borrow Book"
    _inherit = ['mail.thread',
                'mail.activity.mixin'
               ]

    borrower_id=fields.Many2one("library.memberss", domain="[('is_active','=',True)]")

    book_id=fields.Many2many("book.inventory","borrow_book_rel","borrow_id","book_id", domain="[('status','=','available')]")
    author_id=fields.Many2many("res.partner","borrow_author_rel","author_ids","member_ids", domain="[('category_id','=','Author')]")
    borrow_date=fields.Date(default=datetime.today())
    return_validity=fields.Date(default=datetime.today() + timedelta(days=10))
    status=fields.Selection([
        ('borrowed',"Borrowed"),
        ('returned',"Returned"),
    ])
    price=fields.Integer(compute="_get_default_price")

    returned_on=fields.Date()
    total_amount_paid=fields.Float()


    @api.onchange("book_id")
    def get_authors(self):
    #    print("idsss------------------",self.book_id.ids)

       data=self.env["book.inventory"].browse(self.book_id.ids)
       self.author_id = [(6,0,data.author.ids)]


    def action_open_return_book_wizard(self):
           self.ensure_one()
           return{
            'type':'ir.actions.act_window',
            'res_model':'book.return',
            'view_mode': 'form',
            'target' : 'new'
        }
    

    @api.depends("book_id")
    def _get_default_price(self):

         data=self.env["book.inventory"].search([('id','=',self.book_id.ids)])
        #  print("data------------",data)
         total=0
         for i in range(len(data)):
            total=total + data[i].price

         self.price = total


    @api.model_create_multi
    def create(self,vals):
        user_active=self.env["library.memberss"].search([('id','=',vals[0]["borrower_id"])])
        # print("user_active-----------",user_active.is_active)

        if user_active.is_active == True:
            vals[0]['status'] = 'borrowed'
            data=self.env['book.borrow'].search([('borrower_id','=',vals[0]["borrower_id"]),('status','=','borrowed')])
            print("borrower member details---------",vals[0]["book_id"])

            if len(data) >= 3:
                raise UserError("Borrow Limit Reached")
            else:
                find_if_current_book=self.env['book.borrow'].search([('borrower_id','=',vals[0]["borrower_id"]),('status','=','borrowed'),('book_id.id','=',vals[0]['book_id'][0][1])])

                if len(find_if_current_book) >= 1:
                    raise UserError("You Cannot Borrow Same Book Again")
        else:
            raise UserError("Membership is Expired")

        res=super(BorrowBook,self).create(vals)




        return res
    




    #    for i in range(len(data)):
    #         print("author--------",data[i].available_copies)

    #         print("book_id--------",self.book_id.ids)

            # if  data[i].status == "issued":
            #     self.book_id.ids.clear()
            #     raise UserError ("This Book is currently not Available")



    # @api.model_create_multi
    # def create(self, vals):
    #     for rec in vals:

    #         print("self,vals--------",rec["book_id"].id)
    #         print("vals--------",vals)

    #     res=super(BorrowBook,self).create(vals)
    #     return res





    