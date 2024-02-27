import requests
from datetime import datetime
from odoo import models, fields, api

class TypeformResponse(models.Model):
    _name = "typeform.response"
    _description = "Respuestas de Typeform"

    name = fields.Char("Nombre")
    best_erp = fields.Selection([("odoo", "Odoo"), ("sap", "SAP"), ("other", "Otro")], "Mejor ERP")
    year = fields.Integer("Año")
    response_id = fields.Char("ID de la Respuesta")
    response_date = fields.Datetime("Fecha de la Respuesta")

    @api.model
    def update_typeform_data(self, json_response):
        response_data = {
            "name": "",
            "best_erp": "",
            "year": 0,
            "response_id": json_response["response_id"],
            "response_date": datetime.strptime(json_response["submitted_at"], "%Y-%m-%dT%H:%M:%SZ"),
        }

        for answer in json_response["answers"]:
            field_type = answer["type"]
            if field_type == "text":
                response_data["name"] = answer["text"]
            elif field_type == "choice":
                response_data["best_erp"] = answer["choice"]["label"]
            elif field_type == "number":
                response_data["year"] = answer["number"]

        self.create(response_data)
