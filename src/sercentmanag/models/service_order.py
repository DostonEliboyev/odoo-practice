from odoo import models, fields, api

# Buyurtmalar modeli (service.order)
class Order(models.Model):
    _name = 'service.order'
    _description = 'Order Services'

    name = fields.Char( string="Order Name", required=True)
    center_id = fields.Integer( string="Center ")
    customer_id = fields.Char(string="Customer ")
    technician_id = fields.Char(string="Technician")
    order_date = fields.Date(string="Order Date")
    state = fields.Selection([("Draft", "Draft"), ("Received", "Received"), ("Diagnosed", "Diagnosed"), ("Done", "Done"), ("Cancelled", "Cancelled")], string="Status")
    description = fields.Text(string="Description")
    line_ids = fields.Many2many('service.order', string="Lines")
    labor_fee =fields.Float(string="Labor Fee")
    discount_amount = fields.Float(string="Discount Amount")
    payment_ids = fields.Many2many('service.order', string="Payments")
    payment_total =fields.Float(string="Payment Total")
    balance_due =fields.Float(string="Balance Due")
    last_payment_date = fields.Date(string="Last Payment Date")
    rating_ids = fields.Many2many('service.order', string="Ratings")
    total_amount = fields.Float(string="Total Amount")
    is_warranty =fields.Boolean(string="Is Warranty")
    warranty_days = fields.Integer(string="Warranty Days")

