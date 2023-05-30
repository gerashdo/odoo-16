from odoo import models, fields

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offer for an specific property"

    price = fields.Float('Precio')
    status = fields.Selection(
        selection=[
            ('accepted', 'Aceptada'),
            ('refused', 'Rechazada'),
        ],
        string="Estatus",
        copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)