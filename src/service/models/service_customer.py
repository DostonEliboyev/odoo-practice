from odoo import models, fields, api


class Customer(models.Model):
    _name = 'service.customer'
    _description = 'Custom Services'

    name = fields.Char(string="I.F.O", required=True)
    phone =fields.Char(string="Phone")
    email =fields.Char(string="Email")
    center_ids =fields.Char( string="Center")
    order_ids =fields.Char( string="Order")
    payment_ids =fields.Char(string="Payment")
    rating_ids = fields.Char( string="Rating")
    order_count = fields.Integer(string="Order Count")
    active_order_ids = fields.Integer(string="Order Active")
    active_order_count = fields.Integer(string="Order Active")
    done_order_count = fields.Integer(string="Done Order Count")
    total_payment =fields.Integer(string="Total Payment")
    balance_due =fields.Integer(string="Balance Due")
    avg_rating =fields.Float(string="Average Rating")
    last_order_date =fields.Datetime(string="Last Order Date")
    last_payment_date =fields.Datetime(string="Last Payment Date")
