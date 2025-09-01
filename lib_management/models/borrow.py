from odoo import models, fields,api
from datetime import date, timedelta


class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Book Borrowing'
    _inherit=["mail.thread",
              "mail.activity.mixin"]
    prac=fields.Char(string="Example")
    book_id = fields.Many2one('library.book', string="Book", required=True,tracking=True)
    member_id = fields.Many2one('library.member', string="Borrower", required=True,tracking=True)
    borrow_date = fields.Date(string="Borrow Date", default=fields.Date.today,tracking=True)
    return_date = fields.Date(string="Return Date",tracking=True,readonly=0,store=True,compute="_add_return_date")
    state = fields.Selection([
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned')
    ], default='borrowed', string="Status",tracking=True)

    author_id=fields.Many2one("library.author", string="Author")

    t_days=fields.Integer(string="Total Days",store=True,readonly=0,compute="_calculate_days")

# -------------------------------------------------------------------------------------------------------------------
    # @api.model
    # def default_get(self, fields_list):

    #     res = super().default_get(fields_list)

    #     print("=========----------==========",self)
    #     print("=========----------==========",self.env)


    @api.depends('borrow_date','return_date')
    def _add_return_date(self):
        for records in self:
            records.return_date=records.borrow_date + timedelta(days=30)


    @api.depends('return_date')
    def _calculate_days(self):
        for records in self:

            # records.return_date=records.borrow_date + timedelta(days=30)
            if records.borrow_date and records.return_date:
                records.t_days=(records.return_date - records.borrow_date).days
            else:
                 records.t_days= 0 

            
    
    @api.model
    def create(self, vals_list):

        print(f"self---------{self}")
        print(f"val_list---------{vals_list}")


        print("====================----------------=======",self)
        print("ENV====================----------------=======",self.env.context)


    #using search function
        author_nam=self.env["library.book"].search([('id','=',vals_list["book_id"])]).author_id.id
        
    # using browse function
        # val_get=vals_list.get("book_id")
        # print(f"get-----------------{val_get}")
        print(f"self-----------------{self.prac}")
        # a=self.env["library.book"].browse(val_get).author_id.id

        vals_list["author_id"]=author_nam

        # vals_list["prac"] = "Done"

        tags = super(LibraryBorrow, self).create(vals_list)      

        # print(f"id----------------{a}")
        tags.member_id=3

        if tags.return_date == False:
            print(tags.return_date)
            tags.return_date = "2026-05-10"

        print(f"tags-------------------{tags}")
        # print(f"-------------------{vals_list['prac']}")

        return tags



    def write(self,vals):
        print("------Write method called")

        print("vals---------------",vals)

        vals['prac']="Mayank"


        sup_meth=super(LibraryBorrow,self).write(vals)

        




        return sup_meth