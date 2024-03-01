from odoo import models, fields, api

class EstateHouse(models.Model):
    _name = 'estate.house'
    _description = 'Real Estate House'

    name = fields.Char(string='Name', required=True)
    def calculate_price(self):
        pass
