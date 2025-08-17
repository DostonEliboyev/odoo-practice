from odoo import models, fields


class Uzum(models.Model):
    _name = 'uzum.product'
    _description = "Mahsulot haqida malumoti"
    name = fields.Char(string=" Name", required=True)
    description = fields.Text(string="Description", translate=True)
    price = fields.Float(string=" Price", digits=0, required=True)
    price_discount = fields.Integer(string=" Price Discount", digits=0, required=True)
    images = fields.Image(string=" Images file",max_width=1024, max_height=768  )
    comments = fields.Integer(string=" Comments", required=True)
    category = fields.Text(string="Category", required=True)
    like = fields.Integer(string=" Likes", default=0)
    dislike = fields.Integer(string=" Dislikes", default=0)
    warehouseCount = fields.Integer(string=" Warehouse count",default=0)
    salesWeekCount = fields.Integer(string=" Sales Week", default=0)
    isActive = fields.Boolean(string="Foalmi?",)
    # payWithUzumCard = fields.Selection([("witchUzumCard":"Uzum kard bilan"),("anyCard":"boshqa kard bilan ")])

