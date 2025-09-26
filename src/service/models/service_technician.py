from odoo import models, fields, api

# Ustalar modeli (service.technician)
class Technician(models.Model):
    _name = 'service.technician'
    _description = 'Technician'

    name = fields.Char(string="F.I.O  Name", required=True)
    code = fields.Integer( string="Code", )
    description = fields.Text( string="Description")
    is_active = fields.Boolean(string="Is Active")
    country_id = fields.Many2one("service.country", related="center_id.country_id", store=True)
    center_id = fields.Many2one("service.center", related="",string='Center')
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    specialty = fields.Char(string="Specialty")
    hire_date = fields.Date(string="Hire Date")
    capacity_per_day =fields.Float(string="Capacity per Day")
    order_ids = fields.Char( string="Orders")
    active_order_ids = fields.Char( string="Active Orders")
    active_order_count = fields.Integer(string="Active Order Count")
    done_order_ids = fields.Char( string="Done Orders")
    done_order_count = fields.Integer(string="Done Order Count")
    today_order_ids = fields.Char( string="Today Orders")
    today_order_count = fields.Integer(string="Today Order Count")
    utilization_rate =fields.Float(string="Utilization Rate")
    avg_rating =fields.Float(string="Average Rating")
    total_revenue =fields.Float(string="Total Revenue")
    last_order_date = fields.Date(string="Last Order Date")
    is_busy =fields.Boolean(string="Is Busy")


