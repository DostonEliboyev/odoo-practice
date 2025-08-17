from odoo import models, fields
# Dori

class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'clinic.medicine'

    name = fields.Char(string='nomi, umumiy nomi (generic), dozalash birliklari (mg/ml/tablet va h.k.)')
    description = fields.Text(string='tavsif, ')
    manufacturer = fields.Char(string='ishlab chiqaruvchi')
    contraindications =fields.Text(string='kontrendikatsiyalar (boshqa dorilar yoki holatlar bilan mos kelmasligi — matn orqali)')



