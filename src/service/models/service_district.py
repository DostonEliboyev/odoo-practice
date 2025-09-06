from odoo import models, fields, api
# Tumanlar modeli (service.district)

class District(models.Model):
    _name = 'service.district'
    _description = 'District Services'

    name = fields.Char(string='District', required=True)
    code = fields.Char(string='District Code')
    is_active = fields.Boolean(string='Active')
    state_id = fields.Many2one('service.state','State')
    country_id = fields.Many2one('service.country','Country', related="state_id.country_id", store=True)
    center_ids = fields.Char(string='Center')
