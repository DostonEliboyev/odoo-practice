from odoo import models, fields, api
# Tumanlar modeli (service.district)

class District(models.Model):
    _name = 'service.district'
    _description = 'District Services'

    name = fields.Char(string='District', required=True)


