from odoo import models, fields

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag for properties"
    _order = "name"

    name = fields.Char(string="Nombre")

    _sql_constraints = [
        ('name_unique','UNIQUE(name)','El nombre debe ser único')
    ]