from odoo import fields,models,api


class UpdateLeave(models.TransientModel):
    """
    This method will add number of items entered by the user in input 
    existing data will remain unchange
    """
    _name='add.item.number'
    _description="Add Items Number"


    item_num=fields.Integer(string="Number")


    def action_add_items_number(self):
        import random
        import string
         
        data=self.env["sale.order"].browse(self.env.context.get("active_id"))
        # print("data--------------",data.add_item.product_quantity)

        for i in range(self.item_num):
            random_int=random.randint(4,15)
            added_data={
            "item_names" : data.name,
            "product_type": "".join(random.choices(string.ascii_letters, k=random_int)),
            "product_quantity" : random.randint(1,100),
            "product_size" : random.choice(["S","M","XL","XXL","XXXL"])
            }

            data.add_item = [(0,0,added_data)]



class UpdateLeaveSixZero(models.TransientModel):
    """
    This method will add number of items entered by user
    But the existing data will delete first
    """
    _name='add.item.number.sixzero'
    _description="Add Items Number Six Zero"


    item_num=fields.Integer(string="Number")


    def action_add_items_number_sixzero(self):

        import random
        import string
        data=self.env["sale.order"].browse(self.env.context.get("active_id"))

        #Deleting data from model sale.custom.items
        item_list_model=self.env["sale.custom.items"].search([])
        item_list_model.unlink()

        # data.add_item = [(5,0,0)]
        
        for i in range(self.item_num):
            random_int=random.randint(4,15)
            added_data={
            "item_names" : data.id,
            "product_type": "".join(random.choices(string.ascii_letters, k=random_int)),
            "product_quantity" : random.randint(1,100),
            "product_size" : random.choice(["S","M","XL","XXL","XXXL"])
            }

            data.add_item = [(0,0,added_data)]


        
















