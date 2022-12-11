# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property Type'

    name = fields.Char(string="Name", required=True)
    estate_property_ids = fields.One2many('estate.property', 'estate_property_type_id')

    _sql_constraints = [
        ('check_name_is_unique', 'unique(name)',
        'There is a property tag with that name already!')
    ]