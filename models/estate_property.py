# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions
from odoo.tools import date_utils
from odoo.tools import float_utils


class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property'
    _order = "id desc"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(
        string='Date Availability', 
        copy=False, 
        default=lambda self: date_utils.add(fields.Date.today(), months=3))
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price', required=True, copy=False)
    bedrooms = fields.Integer(string='# Of Bedrooms', default=3)
    living_area = fields.Integer(string='Living Areas (sqm)')
    facades = fields.Integer(string='# Of Facades')
    garage = fields.Boolean(string='Has Garage')
    garden = fields.Boolean(string='Has Garden')
    garden_area = fields.Integer(string='# Of Garden Areas')
    garden_orientation = fields.Selection(
        string='Orientation', 
        selection=[('north', 'North'), ('south', 'South'), ('easth', 'Easth'), ('west', 'West')],
        help='This is the orientation of the garden')
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
    
    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0)',
        'The selling price must be higher than zero.'),
        ('check_expected_price', 'CHECK(expected_price > 0)',
        'The expected price must be higher than zero.')
    ]

    total_area = fields.Integer(string="Total Area (sqm)", compute='_total_area')
    best_offer = fields.Float(string="Best Offer", compute='_best_offer')

    estate_property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type")
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer')

    property_tag_ids = fields.Many2many('estate.property.tag', string='Tags')

    property_offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')

    active = fields.Boolean(string='Active', default=True)

    def property_sold(self):
        print("Overriden property sold. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        if self.state == "canceled":
            raise exceptions.UserError("The house is already canceled!")
        else:
            self.state = "sold"

    def property_canceled(self):
        if self.state == "sold":
            raise exceptions.UserError("The house is already sold!")
        else:
            self.state = "canceled"

    def check_offer_accepted(self):
        for offer in self.property_offer_ids:
            if offer.status == 'accepted':
                return True
        return False

    @api.depends('garden_area', 'living_area')
    def _total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    @api.depends('property_offer_ids.price')
    def _best_offer(self):
        for rec in self:
            if not rec.property_offer_ids:
                rec.best_offer = 0
                rec.selling_price = 0
                rec.state = "new"
            else:
                rec.best_offer = max(offer.price for offer in rec.property_offer_ids)

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = None
            self.garden_orientation = None
    
    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for rec in self:
            for offer in rec.property_offer_ids:
                if (offer.status == "accepted") and \
                    (float_utils.float_compare(offer.price, rec.expected_price*0.9, precision_rounding=0.01) == -1):
                    raise exceptions.ValidationError("The accepted offer price is lower than 90%!")
    
    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_canceled(self):
        if any(((prop.state == 'offer recieved') or (prop.state == 'offer accepted') or (prop.state == 'sold')) for prop in self):
            raise exceptions.UserError("Can't delete a property if it is not new or canceled!")