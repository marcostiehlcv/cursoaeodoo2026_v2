from odoo import models, fields, api, _
from datetime import datetime
from datetime import timedelta

class EstateVisit(models.Model):
    _name = "estate.property.visit"
    _description = "Estate Property Visit"
    
    listing_id = fields.Many2one(comodel_name="estate.listing", string="Listing")
    visitor_id = fields.Many2one(comodel_name="res.partner", string="Visitor")
    date = fields.Date(string="Date", default=fields.Date.today())
    note = fields.Text(string="Note")
    agent_id = fields.Many2one(comodel_name="res.users", string="Agent", default=lambda self: self.env.user)
    user_id = fields.Many2one(comodel_name="res.users", string="User", default=lambda self: self.env.user)
    state = fields.Selection(selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('canceled', 'Canceled')], string="State", default="draft")
    

