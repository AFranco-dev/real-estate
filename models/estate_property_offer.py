# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property Offer'

    price = fields.Float(string="Monto", required=True)
    status = fields.Selection(
        string='Offer Status', 
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help='This is the approval status of the order.')
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)