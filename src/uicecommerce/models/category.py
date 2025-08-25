from odoo import models, fields, api


class Category(models.Model):
    _name = 'uicecommerce.category'
    _description = 'uicecommerce.uicecommerce'

    name = fields.Char(string='Name')
    product_count = fields.One2many("uicecommerce.product",string='Products')
    productsCount = fields.Integer(string='Products Count',compute='_compute_products_count')
    #  Categroyiani qanday sanashini bilamdim

    @api.depends('product_count')
    def _compute_products_count(self):
        for product in self:
            print('---', product.productsCount)
            # product.productsCount = product
