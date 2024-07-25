from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required=True)
    phone=fields.Char()
    address=fields.Char()
    part_ids=fields.One2many('model.a','owner_id')