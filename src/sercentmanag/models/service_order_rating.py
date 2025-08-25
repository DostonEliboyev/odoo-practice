from odoo import models, fields, api


class OrderRating(models.Model):
    _name = 'service.order.rating'
    _description = 'Order Rating'

    name = fields.Char(string="Order Rating Name", required=True)
    center_id = fields.Char( string="Center ID")
    order_id = fields.Char(string="Order ID")
    customer_id = fields.Char(string="Customer ID")
    technician_id = fields.Char(string="Technician ID")
    score = fields.Float(string="Score")
    comment = fields.Text(string="Comment")
    rating_date = fields.Date(string="Rating Date")
