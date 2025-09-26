from odoo import models, fields, api

class Orderline(models.Model):
    _name = 'uicecommerce.orderline'
    _description = 'uicecommerce.Orderline'

    product = fields.Char(string="Product")
    value = fields.Integer(string="Value")
    salesprice = fields.Float(string="Salesprice")
    tax = fields.Float(string="Tax")
    discount = fields.Float(string="discount")
    totalprice = fields.Float(string="totalprice")
    profitpercent = fields.Float(string="profitpercent")
    profitmoney = fields.Float(string="profitmoney")
    
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

