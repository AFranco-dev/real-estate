from odoo import api, fields, models, exceptions

class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'salesperson_id', 
        domain = [('date_availability', '<=', fields.Date.today())])