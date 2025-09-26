from odoo import  models, fields, api

class Product(models.Model):
    _name="writelogs.product"
    _description = "Product Model"

    name = fields.Char("Product Name", required=True)
    price = fields.Float("Product Price")
    quantity = fields.Integer("Product Quantity")