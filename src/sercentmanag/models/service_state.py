from odoo import models, fields, api
# Viloyatlar modeli (service.state)

class State(models.Model):
    _name = 'service.state'
    _description = 'State'

    name = fields.Char(string='State', required=True)

