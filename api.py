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
    def update_typeform_data(self):
        token = "tfp_4eVFokNW9JWnZv95cFqExYb6K7yARSHKwroJgoCj3VFW_3pdYxRhPN5xVbR"
        form_id = "ThUFPt1A"
        headers = {"Authorization": f"Bearer {token}"}
        url = f"https://api.typeform.com/forms/{form_id}/responses"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            items = response.json()["items"]
            for item in items:
                response_data = {
                    "name": item["answers"]["short_text"],
                    "best_erp": item["answers"]["choice"]["label"],
                    "year": item["answers"]["number"],
                    "response_id": item["response_id"],
                    "response_date": datetime.strptime(item["submitted_at"], "%Y-%m-%dT%H:%M:%S%z"),
                }
                self.create(response_data)
        else:
            print("Error al obtener las respuestas del formulario")
