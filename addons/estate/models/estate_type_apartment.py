from odoo import models, fields, api

class EstateApartment(models.Model):
    _name = 'estate.apartment'
    _description = 'Real Estate Apartment'

    name = fields.Char(string='Name', required=True)
    def calculate_price(self):
        pass
