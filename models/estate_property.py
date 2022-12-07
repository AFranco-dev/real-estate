# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'estate.property'
    _inherit = []
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price', required=True)
    bedrooms = fields.Integer(string='# Of Bedrooms')
    living_area = fields.Integer(string='# Of Living Areas')
    facades = fields.Integer(string='# Of Facades')
    garage = fields.Boolean(string='Has Garage')
    garden = fields.Boolean(string='Has Garden')
    garden_area = fields.Integer(string='# Of Garden Areas')
    garden_orientation = fields.Selection(
        string='Orientation', 
        selection=[('North', 'north'), ('South', 'south'), ('Easth', 'easth'), ('West', 'west')],
        help='This is the orientation of the garden')