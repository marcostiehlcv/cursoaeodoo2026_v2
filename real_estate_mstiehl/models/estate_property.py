from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    price = fields.Float(string="Price", default=0.0)
    bedrooms = fields.Integer(string="Bedrooms", default=0)
    bathrooms = fields.Integer(string="Bathrooms", default=0)
    garage = fields.Integer(string="Garage", default=0)
    external_url = fields.Char(string="External URL")
    active = fields.Boolean(string="Active", default=True)
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type")
    date_register = fields.Date(string="Date Register", default=fields.Date.today())
    tags_ids = fields.Many2many(comodel_name="estate.property.tag", string="Tags")
    
    
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
    
    name = fields.Char(string="Name", required=True)
    property_id = fields.Many2one(comodel_name="estate.property", string="Property")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    price = fields.Float(string="Price", default=0.0)
    valid = fields.Boolean(string="Valid", default=True)
    active = fields.Boolean(string="Active", default=True)