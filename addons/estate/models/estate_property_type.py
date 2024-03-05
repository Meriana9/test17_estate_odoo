from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Real Estate Property Type'
    _order = "sequence, name"


    name = fields.Char(string='Name', required= True)
    sequence = fields.Integer(string="Sequence")
    property_ids = fields.One2many("estate.property", "type_id", string="Properties")
    
    
    #constraints
    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)', 'Property type name must be unique.'),
    ]    
    