from odoo import fields, models


class HelpdeskBuilding(models.Model):
    _name = "helpdesk.building"
    _description = "Edificio"

    name = fields.Char(string="Nombre", required=True)
    department_ids = fields.One2many(
        string="Áreas",
        comodel_name="helpdesk.department",
        inverse_name="building_id"
    )
