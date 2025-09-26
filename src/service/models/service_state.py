from odoo import models, fields, api
# Viloyatlar modeli (service.state)

class State(models.Model):
    _name = 'service.state'
    _description = 'State'

    name = fields.Char(string='State', required=True)
    code = fields.Char(string='State Code')
    is_active = fields.Boolean(string="Is Active")
    country_id = fields.Many2one( 'service.country','Country',)
    center_ids = fields.Char(string='Centers' )
    district_ids = fields.One2many('service.district','state_id','District Count')
    district_count = fields.Integer(string='District Count')
    center_count = fields.Integer(string='Center Count')
    technician_count = fields.Integer(string='Technician Count')
    active_order_count = fields.Char( string='Active Orders')
    total_revenue = fields.Float(string='Total Revenue')
    avg_rating = fields.Float(string='Average Rating')