from odoo import models, fields, api
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], string='Status', required=True, copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute= '_compute_date_deadline', inverse='_set_date_from_deadline')

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            if offer.create_date:
                offer.date_deadline = offer.create_date + timedelta(days=offer.validity)

    def _set_date_from_deadline(self):
        for offer in self:
            if offer.date_deadline and offer.create_date:
                offer.validity = (offer.date_deadline - offer.create_date).days