from odoo import models, fields

class TypeformResponse(models.Model):
    _name = "typeform.response"
    _description = "Respuestas de Typeform"

    name = fields.Char("Nombre")
    best_erp = fields.Selection([("odoo", "Odoo"), ("sap", "SAP"), ("other", "Otro")], "Mejor ERP")
    year = fields.Integer("Año")
    response_id = fields.Char("ID de la Respuesta")
    response_date = fields.Datetime("Fecha de la Respuesta")
