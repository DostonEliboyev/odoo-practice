from odoo import models, fields

class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    name = fields.Char(required=True)
    author_id = fields.Many2one(comodel_name="library.author", string="Author")
    student_ids = fields.Many2many(comodel_name="library.student", string="borrowed by")


