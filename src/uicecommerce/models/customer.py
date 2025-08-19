
from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Customer(models.Model):
    _name = 'uicecommerce.customer'
    _description = 'uicecommerce.customer'

    name = fields.Char(string='Name')
    lastname = fields.Char(string='Lastname')
    firstname = fields.Char(string='Firstname')
    fullname = fields.Char(string='Fullname',compute="_compute_fullname")
    shortname = fields.Char(string='Fullname',compute="_compute_shortname")
    birthday = fields.Date(string='Birthday', )
    birthday2 = fields.Char(string='Birthday', compute="_compute_birthday")
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    country = fields.Char(string='Country')
    state = fields.Char(string='State')
    city = fields.Char(string='City')
    street = fields.Char(string='Street')
    fulladdress = fields.Char(string='Full Address', compute='_compute_fulladdress')

    buyproduct = fields.Many2many(string="Orders", comodel_name='uicecommerce.product')



    @api.depends('name','lastname','firstname')
    def _compute_fullname(self):
        for record in self:
            record.fullname = f"{record.name} {record.lastname} {record.firstname}"
            record.fullname = f"{record.name} {record.lastname} {record.firstname}"

    @api.depends('name', 'lastname', 'firstname')
    def _compute_shortname(self):
        for record in self:
            if record.name and record.lastname and record.firstname:
                record.shortname = f"{record.name[0]}{record.firstname[0]}{record.lastname[0]}"
            else:
                record.shortname = ''
    @api.depends('country', 'state', 'city','street')
    def _compute_fulladdress(self):
        for record in self:
            record.fulladdress = f"{record.street} {record.city} {record.state} {record.country}"
    @api.depends('birthday')
    def _compute_birthday(self):
        for record in self:
            year = record.birthday.year
            month = record.birthday.month
            day = record.birthday.day
            start_date = datetime(year, month, day)
            today = datetime.today()
            diff = relativedelta(today, start_date)
            record.birthday2 = f"{diff.years} yil {diff.months} oy {diff.days} kun"