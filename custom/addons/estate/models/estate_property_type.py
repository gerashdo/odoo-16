from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Diffrent types for the properties'

    name = fields.Char('Nombre', required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", readonly=True)
    