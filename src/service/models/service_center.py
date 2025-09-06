from odoo import models, fields, api
# Servis Markazi modeli (service.center)

class Center(models.Model):
    _name = 'service.center'
    _description = 'Serves Center'

    name = fields.Char(string="Center Name", required=True)
    description = fields.Text(string="Description")
    code = fields.Integer(string="Center Code",required=True)
    is_active =fields.Boolean(string="Is Active",required=True)

    manager_name = fields.Char(string="Manager")
    capacity_per_day = fields.Float(string="Capacity per Day")
    order_ids = fields.Char( string='Orders')
    payment_ids = fields.Char( string='Payments')
    rating_ids = fields.Char( string='Ratings')
    country_id = fields.Many2one("service.country", related="state_ids.country_ids", store=True)
    technician_ids = fields.One2many("service.technician","center_id" ,string='Technicians')
    technician_count = fields.Char( string='Technicians')
    # Many2many
    active_order_ids = fields.Char( string='Active Orders')
    active_order_count = fields.Integer(string='Active Order Count')
    done_order_ids = fields.Char( string='Done Orders')
    done_order_count = fields.Integer( string="Done Orders Count")
    today_order_ids = fields.Char( string='Today Orders')
    total_revenue = fields.Float(string="Total Revenue")
    avg_rating = fields.Float(string="Average Rating")
    utilization_rate =fields.Float(string="Utilization Rate")
    last_order_date = fields.Date(string="Last Order Date")
