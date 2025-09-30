from odoo import fields,models,api


class ChangeProduct(models.TransientModel):
    _name = 'product.change'
    _description = "Change Product"

    product_id = fields.Many2one("product.product")
    default_code = fields.Char()
    lst_price = fields.Float()
    qty_available = fields.Float()

    sh_replace_prod_id = fields.Many2one("product.product",domain="[('id','in',sh_alternate_products_ids)]")
    sh_alternate_products_ids = fields.Many2many("product.product","current_produc_rel","current_prod","rel_all_prod")


    @api.model
    def default_get(self,vals):
        res=super().default_get(vals)

        active_id=self.env.context.get("active_id")
        data=self.env["sale.order.line"].browse(active_id)

        if "product_id" in vals: 
            res["product_id"] = data.product_id.id

        if "default_code" in vals: 
            res["default_code"] = data.product_id.default_code

        if "lst_price" in vals: 
            res["lst_price"] = data.product_id.lst_price

        if "qty_available" in vals: 
            res["qty_available"] = data.product_id.qty_available
        
        if "sh_alternate_products_ids" in vals:
            res["sh_alternate_products_ids"] = data.product_id.sh_alt_products_ids

        return res
    

    def action_save_product_change(self):
        active_id=self.env.context.get("active_id")
        data=self.env["sale.order.line"].browse(active_id)

        data.write({'product_id': self.sh_replace_prod_id})


    def action_open_view_stock(self):

        data=self.env["sale.order.line"].browse(self.env.context.get('active_id'))

        return {
            'name': f"{data.product_id.name} stock",
            'type' : 'ir.actions.act_window',
            'res_model': 'stock.view.wizard',
            'view_mode':'form',
            'target': 'new',
        }






