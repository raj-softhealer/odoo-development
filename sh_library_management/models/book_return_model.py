from odoo import models,fields,api
from datetime import datetime,timedelta,date
from odoo.exceptions import UserError,ValidationError


class ReturnBook(models.TransientModel):
    _name="book.return"
    _description="Book Return"


    borrower_id=fields.Many2one("library.memberss")
    book_id=fields.Many2many("book.inventory","borrow_book_rel_wizard","borrow_id","book_id")
    author_id=fields.Many2many("res.partner","borrow_author_rel_wizard","author_ids","member_ids", domain="[('category_id','=','Author')]")
    borrow_date=fields.Date()
    return_validity=fields.Date()
    # status=fields.Selection([
    #     ('borrowed',"Borrowed"),
    #     ('returned',"Returned"),
    # ])
    returned_on=fields.Date(default=datetime.today(),readonly=True)
    amount_payable=fields.Float()
    price=fields.Integer()


    @api.model
    def default_get(self,vals):

        res=super(ReturnBook,self).default_get(vals)
        # print("res and self and vals-----------",res,self,vals)
        # print("userss-----------",self.env.context.get("active_id"))


        active_id=self.env.context.get("active_ids",[])
        data=self.env["book.borrow"].browse(active_id)
        # print("data----------",data.borrower_id)

        if "borrower_id" in vals:
            res["borrower_id"] = data.borrower_id

        if "book_id" in vals:
            res["book_id"] = data.book_id

        if "author_id" in vals:
            res["author_id"] = data.author_id

        if "borrow_date" in vals:
            res["borrow_date"] = data.borrow_date

        if "return_validity" in vals:
            res["return_validity"] = data.return_validity

        if "price" in vals:
            res["price"] = data.price
            
        return res
    

    def action_return_book_wizard(self):
        data=self.env["book.borrow"].browse(self.env.context.get("active_id"))
        
        # inventory_data=self.env["book.inventory"].search([('id','=',self.book_id.id)])
        # print("inventory_data---------",inventory_data.available_copies)

        # counter=inventory_data.available_copies+1

        # inventory_data.write({'available_copies': 100})

        if data.status == 'borrowed':
            data.write({'status':'returned'})

        
        if data.borrow_date >= self.returned_on:
            raise ValidationError("Date Should not same or less than to issued date")
        else:
            data.write({"returned_on" : self.returned_on})
            



    @api.onchange("returned_on", "return_validity")
    def _amount_payable_charges(self):
        for rec in self:
             if rec.return_validity < rec.returned_on:
                print(rec.returned_on.day - rec.return_validity.day )
                fine= (rec.price * ((rec.returned_on.day - rec.return_validity.day) *10)) / 100

                rec.amount_payable = fine
             else:
                 rec.amount_payable = 0.0


        
            

