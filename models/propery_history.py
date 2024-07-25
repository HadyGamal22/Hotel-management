from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PropertyHistory(models.Model):
    _name = 'property.history'
    _inherit = ['mail.thread','mail.activity.mixin']#  log  - chatter
    _description='Property history'

    user_id = fields.Many2one('res.users')
    property_id = fields.Many2one('model.a')
    old_state = fields.Char()
    new_state = fields.Char()
    reason = fields.Char()
