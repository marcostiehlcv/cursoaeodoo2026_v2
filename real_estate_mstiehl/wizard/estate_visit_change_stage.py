from odoo import models, fields, api, _


class EstateVisitChangeStage(models.TransientModel):
    _name = "estate.visit.change.stage"
    _description = "Estate Visit Change Stage"

    stage_id = fields.Many2one(comodel_name="estate.stage", string="Stage", domain="[('type_id.code','=','visit')]", required=True)

    def action_change_visit_stage(self):
        visits = self.env["estate.property.visit"].browse(self.env.context.get("active_ids"))
        visits.write({"stage_id": self.stage_id.id})
