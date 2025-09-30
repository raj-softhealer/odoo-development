from odoo import fields,models,api


class ChangeProduct(models.TransientModel):
    _name = 'product.change'
    _description="Change Product"

    product_id=fields.Many2one("product.product")
    default_code=fields.Char()
    lst_price=fields.Float()
    qty_available=fields.Float()

    replace_prod=fields.Many2one("product.product",domain="[('id','in',alternate_products)]")
    alternate_products=fields.Many2many("product.product","current_produc_rel","current_prod","rel_all_prod")




    @api.model
    def default_get(self,vals):
        res=super().default_get(vals)

        active_id=self.env.context.get("active_id")
        data=self.env["sale.order.line"].browse(active_id)

        print(f"\n\n\n data {data.product_id} \n\n ")

        if "product_id" in vals: 
            res["product_id"] = data.product_id.id

        if "default_code" in vals: 
            res["default_code"] = data.product_id.default_code

        if "lst_price" in vals: 
            res["lst_price"] = data.product_id.lst_price

        if "qty_available" in vals: 
            res["qty_available"] = data.product_id.qty_available
        
        if "alternate_products" in vals:
            res["alternate_products"] = data.product_id.alt_products



        return res
    

    

    def action_save_product_change(self):
        active_id=self.env.context.get("active_id")
        data=self.env["sale.order.line"].browse(active_id)

        data.write({'product_id': self.replace_prod})

        print(f"\n\n\n\n self {self} active_id {data.product_id}")



    def action_open_vew_stock(self):

        data=self.env["sale.order.line"].browse(self.env.context.get('active_id'))

        return {
            'name': f"{data.product_id.name} stock",
            'type' : 'ir.actions.act_window',
            'res_model': 'stock.view.wizard',
            'view_mode':'form',
            'target': 'new',
        }






