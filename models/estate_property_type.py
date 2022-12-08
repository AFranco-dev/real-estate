# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property Type'

    name = fields.Char(string="Name", required=True)