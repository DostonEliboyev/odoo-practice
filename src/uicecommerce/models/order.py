from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Order(models.Model):
    _name = 'uicecommerce.order'
    _description = 'uicecommerce.order'

    customer = fields.Char(string="customer")
    delivery_date = fields.Date(string="delivery date")
    delivery_product_count=fields.Char(string="delivery product count",compute="_compute_value_pc")
    product_count=fields.Char(string="product count",compute="_compute_product_count")

    @api.depends('delivery_date')
    def _compute_value_pc(self):
        for record in self:
            year = record.delivery_date.year
            month = record.delivery_date.month
            day = record.delivery_date.day
            start_date = datetime(year, month, day)
            today = datetime.today()
            diff = relativedelta(start_date,today)

            record.delivery_product_count = f"{diff.years} yil {diff.months} oy {diff.days} kun qoldi"
    @api.depends('delivery_product_count')
    def _compute_product_count(self):
        for record in self:
            record.delivery_product_count = f"{record.delivery_product_count}"

