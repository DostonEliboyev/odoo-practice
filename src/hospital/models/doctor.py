from odoo import models, fields
# Shifokor

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital.doctor'

    name = fields.Char('Doctorni ismi')
    specialty= fields.Char("Mutaxasisligi")
    description = fields.Text(string='tajriba yillari, til(lar) bilimi (qisqa ro‘yxat ko‘rinishida saqlash mumkin)')
    workschedule = fields.Date("Ish vaqti")
    cabinetnumber = fields.Char("xona raqami")
    licensenumber = fields.Char("Litsizniya raqami")
    patient = fields.Many2many(comodel_name='hospital.patient',string="Bemor",ondelete="cascade")
