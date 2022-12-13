# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property Type'
    _order = "name"

    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer('Sequence', default=1)

    estate_property_ids = fields.One2many('estate.property', 'estate_property_type_id')
    estate_property_offer_ids = fields.One2many('estate.property.offer', 'property_type_id')

    offers_quantity = fields.Integer(string="Best Offer", compute='_offers_count')

    _sql_constraints = [
        ('check_name_is_unique', 'unique(name)',
        'There is a property tag with that name already!')
    ]

    @api.depends('estate_property_offer_ids')
    def _offers_count(self):
        if self.estate_property_offer_ids:
            return 10
        else:
            return 0

# len(self.estate_property_offer_ids)