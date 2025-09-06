from odoo import models, fields, api

 # Buyurtma qatorlari modeli (service.order.line)

class OrderLine(models.Model):
    _name = 'service.order.line'
    _description = 'Order Line'

    name = fields.Char(string="Order Line Name")
    order_id = fields.Char( string="Order")
    part_id =fields.Char(string="Part")
    description = fields.Char(string="Description")
    note = fields.Text(string="Notes")

