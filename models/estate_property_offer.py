# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions
from odoo.tools import date_utils
from datetime import date


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property Offer'
    _columns={
        'create_date' : fields.Datetime('Creation Date', readonly=True)
    }

    price = fields.Float(string="Amount", required=True)
    status = fields.Selection(
        string='Offer Status', 
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help='This is the approval status of the order.')
    partner_id = fields.Many2one('res.partner', required=True, string="Offerer")
    validity = fields.Integer(string="Validity Days", default=7)

    date_deadline = fields.Date(string="Offer Deadline", compute="_compute_deadline", inverse="_inverse_deadline")

    property_id = fields.Many2one('estate.property', required=True)

    def accept_offer(self):
        if self.property_id.check_offer_accepted():
            raise exceptions.UserError("There is an accepted offer already!")
        else:
            self.status = 'accepted'
    
    def reject_offer(self):
        self.status = 'refused'

    @api.depends('validity')
    def _compute_deadline(self):
        for rec in self:
            if not rec.create_date:
                rec.date_deadline = date_utils.add(date.today(), days = rec.validity)
            else:                
                rec.date_deadline = date_utils.add(date(rec.create_date.year, rec.create_date.month, rec.create_date.day), days = rec.validity)

    def _inverse_deadline(self):
        for rec in self:
            if not rec.create_date:
                rec.validity = (rec.date_deadline - date.today()).days
            else:
                rec.validity = (rec.date_deadline - date(rec.create_date.year, rec.create_date.month, rec.create_date.day)).days