from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    contract_id = fields.Many2one(comodel_name="estate.contract", string="Contract")