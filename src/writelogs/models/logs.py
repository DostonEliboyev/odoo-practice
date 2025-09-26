from odoo import  models,fields

class Logs(models.Model):
    _name = "writelogs.logs"
    _description = "Logs"

    username = fields.Char(string="Log Name")
    message = fields.Text(string="Logs")