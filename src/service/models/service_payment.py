from odoo import models, fields, api

# Buyurtma bo‘yicha qabul qilingan pullar modeli (service.payment)

class Payment(models.Model):
    _name = 'service.payment'
    _description = 'Payment'

    name = fields.Char(string="Name", required=True)
    center_id = fields.Char(string="Center Id")
    order_id = fields.Char(string="Order Id")
    customer_id = fields.Char(string="Customer Id")
    payment_date = fields.Date(string="Payment Date")
    amount = fields.Float(string="Amount")
    note = fields.Text(string="Note")
    state = fields.Selection([('draft', 'Draft'),('confirmed', 'Confirmed'),('cancelled', 'Cancelled')])
    method = fields.Selection([('cash', 'Cash'),('card', 'Card'),('bank', 'Bank')])
    order_total = fields.Float(string="Order Total")
    order_balance_due =fields.Float(string="Order Balance Due")
    customer_total_payment =fields.Float(string="Customer Total")





