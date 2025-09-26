
from odoo import models, fields
# Retsept qatori

class Prescriptionline(models.Model):
    _name = 'hospital.prescriptionline'
    _description = 'clinic.prescriptionline'

    name = fields.Char()
    description = fields.Text(string='qaysi retseptga tegishli')
    medicine= fields.Char(string='dori (medicine)')
    dose = fields.Char(string='dozasi (miqdor + birlik), qabul qilish chastotasi (kuniga necha marta)')
    duration = fields.Integer(string='davomiylik (kun/hafta), izoh')

