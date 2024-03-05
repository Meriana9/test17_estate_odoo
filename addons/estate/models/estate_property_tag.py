from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = 'Real Estate Property Tag'


    name = fields.Char(string='Name', required= True)

#constraints
    _sql_constraints = [
        ('unique_property_tag_name', 'UNIQUE(name)', 'Property tag name must be unique.'),
    ]