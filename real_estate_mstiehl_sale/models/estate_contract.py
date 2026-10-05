from odoo import models, fields, api, _


class EstateContract(models.Model):
    _inherit = "estate.contract"
    
    product_id = fields.Many2one(comodel_name="product.product", string="Product", tracking=True)
   
    order_ids = fields.One2many(comodel_name="sale.order", inverse_name="contract_id", string="Sale Orders") 