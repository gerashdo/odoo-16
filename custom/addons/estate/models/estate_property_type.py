from odoo import models, fields, api

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Diffrent types for the properties'
    _order = "name"

    name = fields.Char('Nombre', required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", readonly=True)
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count", string="Cantidad de ofertas")

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
    