from odoo import fields, models, api
from dateutil.relativedelta import relativedelta 

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Property model'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    postcode = fields.Char('Código Postal')
    date_availability = fields.Date('Fecha de disponibilidad', copy=False, default=fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float('Precio esperado', required=True)
    selling_price = fields.Float('Precio de venta', readonly=True, copy=False)
    bedrooms = fields.Integer('Habitaciones', default=2)
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
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        string='Estado', 
        selection=[
            ('new','New'),
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('canceled','Canceled'),
        ], default='new', required=True, copy=False)
    property_type_id = fields.Many2one("estate.property.type", string="Tipo")
    salesperson = fields.Many2one("res.users", string="Vendedor", default=lambda self: self.env.user)
    buyer = fields.Many2many("res.partner", string="Comprador", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Ofertas")
    