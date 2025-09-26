from reportlab.graphics.transform import translate

from odoo import  models, fields



class Student(models.Model):
    _name = 'school.student'
    _description = "Student malumoti"

    name=fields.Char(string="Student Name" ,required=True)
    bio=fields.Text(string="Student Bio", translate=True)
    age=fields.Integer(string="Student Age", default=16)
    grade=fields.Float(string="Student Grade", )
    birthday=fields.Date(string="Student Birthday", )
    registration_date=fields.Datetime(string="Student Registered", readonly=True)