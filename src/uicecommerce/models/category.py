from odoo import models, fields, api


class Category(models.Model):
    _name = 'uicecommerce.category'
    _description = 'uicecommerce.uicecommerce'

    name = fields.Char(string='Name')
    productsCount = fields.Integer(string='Products Count',compute='_compute_products_count')
    #  Categroyiani qanday sanashini bilamdim
    @api.model
    def _compute_products_count(self):
        for product in self:
            print('---', product.productsCount)
            product.productsCount = product.productsCount + 1
