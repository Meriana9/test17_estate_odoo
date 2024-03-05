from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Real Estate Property Type'


    name = fields.Char(string='Name', required= True)
    
    
    #constraints
    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)', 'Property type name must be unique.'),
    ]    
    