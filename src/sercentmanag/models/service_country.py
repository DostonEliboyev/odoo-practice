from odoo import models, fields, api


class Country(models.Model):
    _name = 'service.country'
    _description = 'Serves Center Country'

    name = fields.Char( string="Center Name", required=True)
    description = fields.Text(string="Description")
    code = fields.Integer(string="Country Code", )
    phone_code = fields.Char(string="Phone Code", )
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    is_active =fields.Boolean(string="Is Active")
    state_ids = fields.Many2many('service.state', string="States")
    center_ids = fields.Many2many('service.center', string="Centers")
    technician_count = fields.Integer()
    state_count = fields.Integer()
    center_count = fields.Integer()
    active_order_count = fields.Integer()
    done_order_ids = fields.Integer()
    done_order_count = fields.Integer()
    total_revenue =fields.Float()
    avg_rating = fields.Float()
    last_order_date = fields.Date()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

