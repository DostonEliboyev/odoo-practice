from reportlab.graphics.transform import translate

from odoo import  models, fields



class Teacher(models.Model):
    _name = 'teacher.student'
    _description = "O'qituvchi malumoti"

    name=fields.Char(string="Teacher Name" ,required=True)
    bio=fields.Text(string="Teacher Bio", translate=True)
    age=fields.Integer(string="Teacher Age", default=25)
    exps=fields.Integer(string="Teacher Tarjibasi", required=True)
    lastWorkPlase=fields.Text(string="Teacher Oxirgi ish joyi", required=True)
    birthday=fields.Date(string="Teacher Birthday")
    registration_date=fields.Datetime(string="Teacher Registered", readonly=True)
