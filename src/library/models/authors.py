
from odoo import models, fields, api


# class Author(models.Model):
#     _name = "library.author"
#     _description = "Author"
#
#     name = fields.Char(required=True)
#     book_ids = fields.One2many(comodel_name="library.book", inverse_name="author_id", string="Books")
#



class Author(models.Model):
    _name = "library.author"
    _description = "Author"

    name = fields.Char(required=True)
    book_ids = fields.One2many(comodel_name="library.book", inverse_name="author_id", string="Books")