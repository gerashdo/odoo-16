from odoo import models, fields

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag for properties"

    name = fields.Char(string="Nombre")