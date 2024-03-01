from odoo import models, fields
from datetime import datetime, timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True, default = 'My new house')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', copy= False, default=lambda self: datetime.today() + timedelta(days=90))
    expected_price = fields.Float(string='Expected Price', required = True )
    selling_price = fields.Float(string='Selling Price', readonly= True)
    bedrooms = fields.Integer(string='Bedrooms' , default = 2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation', default= 'north')


    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(string='Active', default=False)
    
    """ champ stat """
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='State', required=True, default='new', copy=False)
    
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)