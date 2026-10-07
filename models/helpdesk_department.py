from odoo import fields, models


class HelpdeskDepartment(models.Model):
    _name = "helpdesk.department"
    _description = "Oficina"

    name = fields.Char(string="Nombre", required=True)
    building_id = fields.Many2one(
        string="Edificio",
        comodel_name="helpdesk.building",
        required=True
    )
