from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"
    _order = "date_register desc"
    _rec_name = "name"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(string="Name", required=True, tracking=True)
    description = fields.Text(string="Description", tracking=True)
    image_1920 = fields.Image("Primary Image", max_width=1920, max_height=1920)
    cunstruction_year = fields.Integer(string="Construction Year", tracking=True)
    
    seller_id = fields.Many2one(comodel_name="res.partner", string="Seller", tracking=True)
    agent_id = fields.Many2one(comodel_name="res.partner", string="Agent", tracking=True)
    
    google_maps_url = fields.Char(string="Google Maps URL")
    postcode = fields.Char(string="Postcode", tracking=True)
    address = fields.Char(string="Address", tracking=True)
    country_id = fields.Many2one(comodel_name="res.country", string="Country", default=1, tracking=True)
    # city_id = fields.Many2one(comodel_name="res.city", string="City", tracking=True)
    
    expected_price = fields.Float(string="Expected Price", default=0.0, tracking=True)
    selling_price = fields.Float(string="Selling Price", default=0.0, readonly=True, tracking=True)
    
    total_area = fields.Float(string="Total Area", default=0.0, tracking=True)
    living_area = fields.Integer(string="Living Area", default=0, tracking=True)
    bedrooms = fields.Integer(string="Bedrooms", default=0, tracking=True)
    bathrooms = fields.Integer(string="Bathrooms", default=0, tracking=True)
    garage = fields.Integer(string="Garage", default=0, tracking=True)
    garden = fields.Integer(string="Garden", default=0, tracking=True)
    garden_orientation = fields.Selection(selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Garden Orientation", default='north', tracking=True)
    garden_area = fields.Float(string="Garden Area", default=0.0, tracking=True)
    
    external_url = fields.Char(string="External URL")
    
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type", tracking=True)
    property_category_id = fields.Many2one(comodel_name="estate.property.category", string="Property Category", tracking=True)
    
    date_register = fields.Date(string="Date Register", default=fields.Date.today())
    date_sold = fields.Date(string="Date Sold", readonly=True)
        
    tags_ids = fields.Many2many(comodel_name="estate.property.tag", string="Tags")
    offers_ids = fields.One2many(comodel_name="estate.property.offer", inverse_name="property_id", string="Offers")
    gallery_ids = fields.One2many(comodel_name="estate.property.gallery", inverse_name="property_id", string="Gallery")
    contacts_ids = fields.One2many(comodel_name="estate.property.contacts", inverse_name="property_id", string="Contacts")
    
    active = fields.Boolean(string="Active", default=True, tracking=True)
    available = fields.Boolean(string="Available", default=True, tracking=True)
    published = fields.Boolean(string="Published", default=False, tracking=True)
    
    
class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    active = fields.Boolean(string="Active", default=True)
    
    
class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
    active = fields.Boolean(string="Active", default=True)
    

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _rec_name = "property_id"
    
    property_id = fields.Many2one(comodel_name="estate.property", string="Property")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    price = fields.Float(string="Price", default=0.0)
    valid = fields.Boolean(string="Valid", default=True)
    active = fields.Boolean(string="Active", default=True)
    

class EstatePropertyGallery(models.Model):
    _name = "estate.property.gallery"
    _description = "Estate Property Gallery"
    
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    property_id = fields.Many2one(comodel_name="estate.property", string="Property")
    image = fields.Image("Image", max_width=1920, max_height=1920)
    

class EstatePropertyContacts(models.Model):
    _name = "estate.property.contacts"
    _description = "Estate Property Contacts"
    
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    property_id = fields.Many2one(comodel_name="estate.property", string="Property")
    role_id = fields.Many2one(comodel_name="estate.property.contacts.role", string="Role")
    

class EstatePropertyContactsRole(models.Model):
    _name = "estate.property.contacts.role"
    _description = "Estate Property Contacts Role"
    
    name = fields.Char(string="Name", required=True)


class EstatePropertyCategory(models.Model):
    _name = "estate.property.category"
    _description = "Estate Property Category"
    
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    active = fields.Boolean(string="Active", default=True)