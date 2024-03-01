from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Real Estate Property Type'


    name = fields.Char(string='Name', required= True)
""" type = fields.Char(string='Char')
attributes = fields.Char( required=True) """
    
    