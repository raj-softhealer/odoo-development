from odoo import fields,models,api

class AlternativePeoducts(models.Model):
    _inherit="product.product"


    alt_products=fields.Many2many("product.product",
                                  "product_to_product_rel",
                                  "current_product_ids",
                                  "prodcuts_product_ids",
                                  string="Select Alternate Products",
                                  domain="[('id','!=',id)]")
    

    def write(self,vals):
         '''
         This method will interconnect all record items on adding in field 
         'alt_products' and  while remove record item it will remove current 
         record from opposite side too  
         '''
        #  print(f"\n\n\n old self {self.alt_products}")
         print(f"\n\n\n\n\n\n write callllllledddddd \n\n\n\n")

         old_prodct_data=self.alt_products

         res=super().write(vals)

        #  print("\n\n\n",self.alt_products)
         
         temp_data=self.alt_products.ids
         temp_data.append(self.id)

         for prod in self.alt_products:
             for t in temp_data:
                 if  t != prod.id and t not in prod.alt_products.ids:
                        prod.write({'alt_products':[(4,t)]})

        #  print(f"\n\n\n new self {self.alt_products}")

         new_prodct_data=self.alt_products

         for old in old_prodct_data:
              if old not in new_prodct_data:
                #    print(f"\n\n\n self {self.id} \n\n\n")
                   old.write({'alt_products': [(3,self.id)]})
                   
                # old.alt_products.unlink(self.id)
                      

         return res   
    


    def action_open_view_stock_alternate_product(self):
        
        print(f"\n\n\n {self.id}")
        
        return {
            'name': f"{self.name} stock",
            'type' : 'ir.actions.act_window',
            'res_model': 'stock.view.wizard',
            'view_mode':'form',
            'target': 'new',
        }
