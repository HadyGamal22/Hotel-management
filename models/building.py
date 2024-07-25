from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Building(models.Model):
    _name = 'building'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description='Building'
    _rec_name='code'

    no =fields.Integer()
    code=fields.Char()
    active=fields.Boolean(default=True)
    name=fields.Char()
    description=fields.Text()