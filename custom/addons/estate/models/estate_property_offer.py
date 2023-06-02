from odoo import models, fields, api, exceptions
from dateutil.relativedelta import relativedelta 

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
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Date.today()
            days = record.validity or 0
            record.date_deadline = create_date + relativedelta(days=days)

    def _inverse_date_deadline(self):
        for record in self:
            creation_date = fields.Date.from_string(record.create_date) or fields.Date.today()
            end_date = fields.Date.from_string(record.date_deadline)
            record.validity = (end_date - creation_date).days 

    def accept_offer(self):
        for record in self:
            if not record.status == 'refused':
                record.status = 'accepted'
                record.property_id.selling_price = record.price
                record.property_id.buyer = record.partner_id
            else:
                raise exceptions.UserError('La oferta ya ha sido rechazada')
        
        return True
    
    def reject_offer(self):
        for record in self:
            if not record.status == 'accepted':
                record.status = 'refused'
            else:
                raise exceptions.UserError('La oferta ya ha sido aceptada')