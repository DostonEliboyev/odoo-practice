from odoo import models, fields, api

# Detallar modeli (service.part)
class Part(models.Model):
    _name = 'service.part'
    _description = 'Service Part'

    name = fields.Char( string="Part Name", required=True)
    code = fields.Char( string="Part Code", required=True)
    is_active =fields.Boolean(string="Is Active")
    description = fields.Text(string="Description")


