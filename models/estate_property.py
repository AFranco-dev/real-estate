# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import date_utils


class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(
        string='Date Availability', 
        copy=False, 
        default=lambda self: date_utils.add(fields.Date.today(), months=3))
    expected_price = fields.Float(string='Expected Price', readonly=True)
    selling_price = fields.Float(string='Selling Price', required=True, copy=False)
    bedrooms = fields.Integer(string='# Of Bedrooms', default=3)
    living_area = fields.Integer(string='# Of Living Areas')
    facades = fields.Integer(string='# Of Facades')
    garage = fields.Boolean(string='Has Garage')
    garden = fields.Boolean(string='Has Garden')
    garden_area = fields.Integer(string='# Of Garden Areas')
    garden_orientation = fields.Selection(
        string='Orientation', 
        selection=[('north', 'North'), ('south', 'South'), ('easth', 'Easth'), ('west', 'West')],
        help='This is the orientation of the garden')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        string='State Of Property', 
        selection=[
            ('new', 'New'), 
            ('offer recieved', 'Offer Recieved'), 
            ('offer accepted', 'Offer Accepted'), 
            ('sold', 'Sold'), 
            ('canceled', 'Canceled')],
        help='Select the state in wich the property is.',
        required=True, 
        copy=False, 
        default='new')

    estate_property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type")

    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer')

    property_tag_ids = fields.Many2many('estate.property.tag', string='Tags')

    property_offer_ids = fields.One2many('estate.property.offer', string='Offers')