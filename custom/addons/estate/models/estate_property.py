from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Property model'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    postcode = fields.Char('Código Postal')
    date_availability = fields.Date('Fecha de disponibilidad')
    expected_price = fields.Float('Precio esperado', required=True)
    sellig_price = fields.Float('Precio de venta')
    bedrooms = fields.Integer('Habitaciones')
    living_area = fields.Integer('Área')
    facades = fields.Integer('Fachada')
    garage = fields.Boolean('Cochera')
    garden = fields.Boolean('Jardin')
    garden_area = fields.Integer('Área del jardin')
    garden_orientation = fields.Selection(
        string='Orientación del jaardin',
        selection=[
            ('north','Norte'),
            ('south','Sur'),
            ('east','Este'),
            ('west','Oeste')
        ])