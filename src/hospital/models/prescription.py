from odoo import models, fields
# Retsept

class Prescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'clinic.prescription'

    name = fields.Char(string='prescription name')
    doctor = fields.Char(string='doctor name')
    patientwritetime = fields.Date()
    description = fields.Text(string='umumiy ko‘rsatmalar (masalan, “yoki ovqatdan keyin ichilsin”, “7 kun”)')



