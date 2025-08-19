from odoo import models, fields, api

class Product(models.Model):
    _name = 'uicecommerce.product'
    _description = 'uicecommerce.product'

    name = fields.Char()
    slug =  fields.Char()
    category_id = fields.Many2one('uicecommerce.category', string='Category')
    salesprice = fields.Integer()
    price = fields.Integer()
    percentage = fields.Float(compute="_compute_sales_price", string="Sales Price Proft")
    width = fields.Integer()
    height = fields.Integer()
    length = fields.Integer()
    size = fields.Text('Hajmi',compute='_compute_size')

    @api.depends('price','salesprice')
    def _compute_sales_price(self):
        for record in self:
            if record.salesprice and record.price:
                record.percentage =100- ( record.price * 100)/record.salesprice
            else:
                record.percentage = 0
    @api.depends('width','height','length')
    def _compute_size(self):
        for record in self:
            record.size= record.width*record.height*record.length

    # @api.depends('name')
    # def _compute_slug(self):
    #     for record in self:
    #         print(record)
    #         if record.name:
    #             record.slug = record.sub(r'[^a-zA-Z0-9]+', '-', record.name.lower()).strip('-')
    #         else:
    #             record.slug = ''