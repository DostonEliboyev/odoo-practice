from odoo import models, fields, api
# Servis Markazi modeli (service.center)

class Center(models.Model):
    _name = 'service.center'
    _description = 'Serves Center'

    name = fields.Char(string="Center Name", required=True)
    description = fields.Text(string="Description")
    code = fields.Integer(string="Center Code",required=True)
    is_active =fields.Boolean(string="Is Active",required=True)
    country_id = fields.Many2one('service.country', string='Country')
    state_id = fields.Many2one('service.state', string='State')
    district_id = fields.Many2one('service.district', string='District')
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")
    manager_name = fields.Char(string="Manager")
    capacity_per_day = fields.Float(string="Capacity per Day")
    order_ids = fields.Many2many('service.order', string='Orders')
    payment_ids = fields.Many2many('service.payment', string='Payments')
    rating_ids = fields.Many2many('service.order.rating', string='Ratings')
    technician_count = fields.Many2many('service.technician', string='Technicians')
    active_order_ids = fields.Many2many('service.order', string='Active Orders')
    active_order_count = fields.Integer(string='Active Order Count')
    done_order_ids = fields.Many2many('service.order', string='Done Orders')
    done_order_count = fields.Integer( string="Done Orders Count")
    today_order_ids = fields.Many2many('service.order', string='Today Orders')
    total_revenue = fields.Float(string="Total Revenue")
    avg_rating = fields.Float(string="Average Rating")
    utilization_rate =fields.Float(string="Utilization Rate")
    last_order_date = fields.Date(string="Last Order Date")




    value2 = fields.Float(compute="_value_pc", store=True)
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

