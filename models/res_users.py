from odoo import api, fields, models, exceptions

class EstateProperty(models.Model):
    _inherit = ['res.users']

    property_ids = fields.One2many('estate.property', 'salesperson_id', 
        domain = [('date_availability', '&lt;=', fields.Date.today())])