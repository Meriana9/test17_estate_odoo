from odoo import models, fields, api

class EstateCastle(models.Model):
    _name = 'estate.castle'
    _description = 'Real Estate Castle'

    name = fields.Char(string='Name', required=True)
    def calculate_price(self):
        pass
