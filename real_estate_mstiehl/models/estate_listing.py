from odoo import models, fields, api, _
from datetime import datetime
from datetime import timedelta

class EstateListing(models.Model):
    _name = "estate.listing"
    _description = "Estate Listing"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date_register desc"
    
    name = fields.Char(string="Name", required=True, tracking=True)
    property_id = fields.Many2one(comodel_name="estate.property", string="Property", tracking=True)
    listing_ref_code = fields.Char(string="Listing Code", store=True, tracking=True, readonly=True)
    type_id = fields.Many2one(comodel_name="estate.listing.type", string="Type")
    description = fields.Text(string="Description", tracking=True)
    seller_id = fields.Many2one(comodel_name="res.partner", string="Seller", tracking=True)
    agent_id = fields.Many2one(comodel_name="res.users", string="Agent", tracking=True)
    expected_price = fields.Float(string="Expected Price", default=0.0, tracking=True)
    selling_price = fields.Float(string="Selling Price", default=0.0, readonly=True, tracking=True)
    state = fields.Selection(selection=[('draft', 'Draft'), ('published', 'Published'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('reserved', 'Reserved'), ('sold', 'Sold'), ('canceled', 'Canceled')], string="State", default="draft")
    date_register = fields.Date(string="Date Register", default=fields.Date.today())
    date_published = fields.Date(string="Date Published", readonly=True)
    date_offer_received = fields.Date(string="Date Offer Received", readonly=True)
    date_offer_accepted = fields.Date(string="Date Offer Accepted", readonly=True)
    date_reserved = fields.Date(string="Date Reserved", readonly=True)
    date_sold = fields.Date(string="Date Sold", readonly=True)
    date_canceled = fields.Date(string="Date Canceled", readonly=True)
    external_url = fields.Char(string="External URL")
    active = fields.Boolean(string="Active", default=True)
    tags_ids = fields.Many2many(comodel_name="estate.tag", string="Tags")
    offer_ids = fields.One2many(comodel_name="estate.listing.offer", inverse_name="listing_id", string="Offers")

    user_id = fields.Many2one(comodel_name="res.users", string="User", default=lambda self: self.env.user)
    
    @api.model_create_multi
    def create(self, vals_list):
        context = self._context
        vals_list[0]["listing_ref_code"] = f"LIST#{(datetime.today()).strftime('%y%m%d%H%M%S')}"            
        return super(EstateListing, self).create(vals_list)
    

class EstateListingType(models.Model):
    _name = "estate.listing.type"
    _description = "Estate Listing Type"
    
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    active = fields.Boolean(string="Active", default=True)
    
    
class EstateListingOffer(models.Model):
    _name = "estate.listing.offer"
    _description = "Estate Listing Offer"
    _rec_name = "listing_id"
    
    listing_id = fields.Many2one(comodel_name="estate.listing", string="Listing")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    price = fields.Float(string="Price", default=0.0)
    valid = fields.Boolean(string="Valid", default=True)
    valid_until = fields.Date(string="Date Valid", default=fields.Date.today() + timedelta(days=7))
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(selection=[('submitted', 'Submitted'), ('in_analysis', 'In Analysis'),('accepted', 'Accepted'), ('refused', 'Refused'), ('expired', 'Expired')], string="State", default="submitted")
    date = fields.Date(string="Date", default=fields.Date.today())
    date_in_analysis = fields.Date(string="Date In Analysis")
    date_accepted = fields.Date(string="Date Accepted")
    date_refused = fields.Date(string="Date Refused")
    date_expired = fields.Date(string="Date Expired")
    
    user_id = fields.Many2one(comodel_name="res.users", string="User", default=lambda self: self.env.user)
    
    def action_in_analysis(self):
        for record in self:
            record.state = "in_analysis"
            record.date_in_analysis = fields.Date.today()
            
    def action_accepted(self):
        for record in self:
            record.state = "accepted"
            record.date_accepted = fields.Date.today()
    
    def action_refused(self):
        for record in self:
            record.state = "refused"
            record.date_refused = fields.Date.today()
            
    def action_expired(self):
        for record in self:
            record.state = "expired"
            record.date_expired = fields.Date.today()