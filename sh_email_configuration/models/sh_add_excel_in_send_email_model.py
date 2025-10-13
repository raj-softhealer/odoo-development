from odoo import fields,models,api
import io
import base64
import xlsxwriter


class AddExcelFile(models.TransientModel):
    _inherit = "mail.compose.message"


    def default_get(self,vals):
    
        res=super().default_get(vals)
        

        data=self.env["sale.order"].browse(self.env.context.get("active_id"))
        
        file = io.BytesIO()
        workbook = xlsxwriter.Workbook(file, {'in_memory': True})
        worksheet = workbook.add_worksheet('Sale Order Items')

        header_design = workbook.add_format({'bold': True, 'bg_color': "#5AC3C7"})
        worksheet.write(0, 0, 'Product Name', header_design)
        worksheet.write(0, 1, 'Quantity', header_design)
        worksheet.write(0, 2, 'Delivered', header_design)
        worksheet.write(0, 3, 'Invoiced', header_design)
        worksheet.write(0, 4, 'Unit Price', header_design)
        worksheet.write(0, 5, 'Taxes', header_design)
        worksheet.write(0, 6, 'Amount', header_design)
                 
        row = 1

        for order_items in data.order_line:
            worksheet.write(row, 0, order_items.product_id.name)  
            worksheet.write(row, 1, order_items.product_uom_qty)  
            worksheet.write(row, 2, order_items.qty_delivered)  
            worksheet.write(row, 3, order_items.qty_invoiced)  
            worksheet.write(row, 4, order_items.price_unit)  
            # worksheet.write(row, 5, line.tax_id.mapped("data.order_line"))  
            worksheet.write(row, 6, order_items.price_subtotal)  
            row += 1
              

        workbook.close()
        file.seek(0)

        attr=self.env['ir.attachment'].create({
        'name': f"{data.name}_report.xlsx",
        'type': 'binary',
        'datas': base64.b64encode(file.read()),
        'res_model': data._name,
        'res_id': data.id,
        })
        
        template_id = self.env["mail.template"].browse(self.env.context.get("default_template_id"))

        if not template_id.attachment_ids:
            template_id.attachment_ids = [(4,attr.id)]

        return res