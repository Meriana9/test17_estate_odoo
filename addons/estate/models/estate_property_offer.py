from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError

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
                
            
    def action_accept_offer(self):
        properties = self.mapped('property_id')
        for prop in properties:
            accepted_offers = self.env['estate.property.offer'].search([('property_id', '=', prop.id), ('state', '=', 'accepted')])
            if len(accepted_offers) > 0:
                raise UserError("Only one offer can be accepted for a property!")
        for offer in self:
            offer.property_id.buyer_id = offer.buyer_id
            offer.property_id.selling_price = offer.price
            offer.property_id.state = 'offer_accepted'
            
    def action_refuse_offer(self):
        for offer in self:
            offer.state = 'refused'            