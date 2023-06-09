from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def set_as_sold(self):
        result = super().set_as_sold()
        invoices_list = []
        
        for property in self:
            invoices_list.append({
                "partner_id": property.buyer.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    Command.create({
                        "name": property.name,
                        "quantity": 1.0,
                        "price_unit": property.selling_price * 0.06
                    }),
                    Command.create({
                        "name": "Administrative fees",
                        "quantity": 1.0,
                        "price_unit": 100.0
                    })
                ]
            })

        self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoices_list)
        return result