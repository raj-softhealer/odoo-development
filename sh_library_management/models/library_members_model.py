from odoo import fields,models,api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

class LibraryMembers(models.Model):
    _name="library.memberss"
    _rec_name="members_id"
    _description="Library Member"
    _inherit = ['mail.thread',
                'mail.activity.mixin'
               ]



    members_id=fields.Many2one("res.users", string="Name", required=True)
    member_from=fields.Date(string="Member from", default=datetime.today())
    member_to=fields.Date(string="To")
    borrow_history=fields.One2many("book.borrow","borrower_id")
    is_active=fields.Boolean(string="Active", compute="_is_user_active", store=True)

    @api.onchange("member_from")
    def member_subscription(self):
        self.member_to=self.member_from + relativedelta(years=1)

        for rec in self:
            # print(rec.member_to < date.today())
            if rec.member_to < date.today():
                rec.is_active = False
            else:
                rec.is_active = True


    @api.depends("member_to")
    def _is_user_active(self):
            print(self.member_to < date.today())
            if self.member_to < date.today():
                 self.is_active = False
            else:
                 self.is_active = True

    
    