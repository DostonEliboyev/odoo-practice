from odoo import models, fields, api


class Country(models.Model):
    _name = 'service.country'
    _description = 'Serves Center Country'

    name = fields.Char( string="Center Name", required=True)
    description = fields.Text(string="Description")
    code = fields.Integer(string="Country Code", )
    phone_code = fields.Char(string="Phone Code", )
    value = fields.Integer()
    is_active =fields.Boolean(string="Is Active")
    state_ids = fields.One2many('service.state', 'country_id',"States",)
    district_ids = fields.One2many('service.district',"country_id","Districts")
    center_ids = fields.Many2many('service.center', string="Centers")
    technicians = fields.Many2many("service.technician", string="Technicians")
    technician_count = fields.Integer()
    state_count = fields.Integer()
    center_count = fields.Integer()
    active_order_count = fields.Integer()
    done_order_ids = fields.Integer()
    done_order_count = fields.Integer()
    total_revenue =fields.Float()
    avg_rating = fields.Float()
    last_order_date = fields.Date()


    def _compute_technicians(self):
        tech_count = self.env['service.technician'].search_count([])