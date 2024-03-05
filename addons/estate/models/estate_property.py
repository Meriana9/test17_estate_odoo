from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

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
    garden_area = fields.Integer(string='Garden Area')
    total_area = fields.Integer(string="Total Area", compute='_compute_total_area')
    best_price = fields.Float(string='Best Price', compute='_compute_best_price', store=True)

    """ champ total area """
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area
            
    """ champ best offer """
    @api.depends('property_offer_ids.price')
    def _compute_best_price(self):
        for property_record in self:
            if property_record.property_offer_ids:
                property_record.best_price = max(property_record.property_offer_ids.mapped('price'))
            else:
                property_record.best_price = 0.0
            
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation', default= 'north')

    """ méthod apappelée lorsqu'il y a un changement dans le champ "garden" """
    
    
    @api.onchange('garden')
    def onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation= 'north'
        else:
            self.garden_area = 0
            self.garden_orientation=  False
        

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
    
            
    def action_cancel_property(self):
        if self.state == 'sold':
            raise UserError("A sold property cannot be canceled.")
        self.state = 'canceled'
        
    
    def action_sell_property(self):
        if self.state == 'canceled':
            raise UserError("A canceled property cannot be sold.")
        self.state = 'sold'

# constraint
    _sql_constraints = [
        ('positive_expected_price', 'CHECK(expected_price > 0)', 'Expected price must be strictly positive.'),]

    # se délanche à chaque fois y un changement de price
    @api.constrains('expected_price', 'selling_price')
    def _check_selling_price(self):
        for record in self:
            # Ignore when the selling price is zero (not set yet)
            if not float_is_zero(record.selling_price, precision_digits=2):
                continue
            min_selling_price = 0.9 * record.expected_price
            if float_compare(record.selling_price, min_selling_price, precision_digits=2) < 0:
                raise ValidationError("Selling price cannot be lower than 90% of the expected price")

    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id= fields.Many2one('res.partner', string="Buyer")
    salesperson_id= fields.Many2one('res.users', string="Salesperson", default=lambda self: self.env.user)
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    property_offer_ids = fields.Many2many("estate.property.offer", 'property_id', string="offers")
    

"""   
    def action_cancel_property(self):
        for property_record in self:
            if property_record.state != 'sold':
                property_record.state = 'canceled' 
                
                    
    def action_cancel_property(self):
        if self.state == 'sold':
            raise UserError("A sold property cannot be canceled.")
        self.state = 'canceled'
                """