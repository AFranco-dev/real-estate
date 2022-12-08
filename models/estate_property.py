# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import date_utils


class HospitalPatient(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(string='Date Availability', copy=False, default=lambda self: date_utils.add(fields.Date.today(), months=3))
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price', required=True, readonly=True, copy=False)
    bedrooms = fields.Integer(string='# Of Bedrooms', default=3)
    living_area = fields.Integer(string='# Of Living Areas')
    facades = fields.Integer(string='# Of Facades')
    garage = fields.Boolean(string='Has Garage')
    garden = fields.Boolean(string='Has Garden')
    garden_area = fields.Integer(string='# Of Garden Areas')
    garden_orientation = fields.Selection(
        string='Orientation', 
        selection=[('North', 'north'), ('South', 'south'), ('Easth', 'easth'), ('West', 'west')],
        help='This is the orientation of the garden')