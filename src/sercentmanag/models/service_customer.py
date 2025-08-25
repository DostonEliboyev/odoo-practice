from odoo import models, fields, api


class Customer(models.Model):
    _name = 'service.customer'
    _description = 'Custom Services'

    name = fields.Char(string="I.F.O", required=True)
    phone =fields.Char(string="Phone")
    email =fields.Char(string="Email")
    center_ids =fields.Many2one('service.center', string="Center")
    order_ids =fields.Many2one('service.order', string="Order")
    payment_ids =fields.Many2one('service.payment', string="Payment")
    rating_ids = fields.Many2one('service.order.rating', string="Rating")
    order_count = fields.Integer(string="Order Count")
    active_order_ids = fields.Integer(string="Order Active")
    active_order_count = fields.Integer(string="Order Active")
    done_order_count = fields.Integer(string="Done Order Count")
    total_payment =fields.Integer(string="Total Payment")
    balance_due =fields.Integer(string="Balance Due")
    avg_rating =fields.Float(string="Average Rating")
    last_order_date =fields.Datetime(string="Last Order Date")
    last_payment_date =fields.Datetime(string="Last Payment Date")
