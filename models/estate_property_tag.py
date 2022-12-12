# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property Tag'
    _order = "name"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('check_name_is_unique', 'unique(name)',
        'There is a property type with that name already!')
    ]