# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import date_utils


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property Offer'

    price = fields.Float(string="Amount", required=True)
    status = fields.Selection(
        string='Offer Status', 
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help='This is the approval status of the order.')
    partner_id = fields.Many2one('res.partner', required=True, string="Offerer")
    validity = fields.Integer(string="Validity Days", default=7)

    date_deadline = fields.Date(string="Offer Deadline", compute="_compute_deadline", inverse="_inverse_deadline")

    property_id = fields.Many2one('estate.property', required=True)

    @api.depends('validity', 'date_deadline')
    def _compute_deadline(self):
        for rec in self:
            rec.date_deadline = date_utils.add(fields.Date.today(), days = rec.validity)

    def _inverse_deadline(self):
        for rec in self:
            rec.validity = date_utils.subtract(rec.date_deadline, fields.Date.today()).days
