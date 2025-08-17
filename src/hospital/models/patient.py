from datetime import date

from odoo import models, fields,api
# Bemor

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'hospital.patient'

    name = fields.Char("Bemorni ismi")
    birthday = fields.Date("Tug'ilgan sanasi")
    phonenumber = fields.Char("telefon nomeri")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    description = fields.Text("umumiy malumoti")
    doctor = fields.Many2many(comodel_name='hospital.doctor',string="Doctor",ondelete="cascade")
    appointment = fields.Many2one(comodel_name='hospital.appointment',string="Biriktirlgan xonasi")
    birthday_count = fields.Integer(compute="_compute_birthday_count",string="Yoshi")
    prescription = fields.Many2many(comodel_name='hospital.prescription', string="Biriktirlgan Dorilar")

    @api.depends("birthday")
    def _compute_birthday_count(self):
         for record in self:
             # record.birthday_count = 1
             record.birthday_count = date.today().year - record.birthday.year


