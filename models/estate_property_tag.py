# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property Tag'

    name = fields.Char(string="Name", required=True)