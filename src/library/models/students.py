from odoo import models, fields
# class Students(models.Model):
#     _name = 'library.students'
#     _description = 'Students'
#
#     name = fields.Char()
#     id_number = fields.Char()
#     description = fields.Text()
#     book_ids = fields.Many2one('library.books', string='Books')
#


class Student(models.Model):
        _name = "library.student"
        _description = "Student"

        name = fields.Char(required=True)
        borrowed_book_ids = fields.Many2many(comodel_name="library.book", string="Borrowed Books")

