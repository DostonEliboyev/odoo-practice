from odoo import models, fields
# Qabul

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'clinic.appointment'

    name = fields.Char("Appointment Name")
    appointmentnumber = fields.Char("Appointment Number")
    description = fields.Text("Umumiy malumoti")
    patient = fields.Char()
    doctor = fields.Char()
    status = fields.Selection([('new', 'New'), ('confirmed', 'Confirmed'),('canceled','Canceled'),('completed','Completed')])
    diagnosis = fields.Text()
    startendtime = fields.Date()


