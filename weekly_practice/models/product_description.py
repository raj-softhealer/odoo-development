from odoo import models,fields,api
from lxml import html
class ProductDescription(models.Model):
    _inherit="sale.order.line"


    product_descrition=fields.Html(string="Product Description")


    @api.onchange("product_template_id")
    def _add_description_action(self):
        """
        This method will find the description field from product.template and 
        will add in the product_descirption which is defined above in sale > quotation"""

        # print("-------------",html.fromstring(res.description).text_content())

        # Get description field from product.template to add in product description
        for rec in self:
            print("self-----------",self.product_template_id.description)
            data=self.product_template_id.description
            # res = self.env["product.template"].search([('id','=',self.product_template_id.id)])
            rec.product_descrition = html.fromstring(data).text_content()
            rec.product_descrition = self.product_template_id.description
            
            

        

