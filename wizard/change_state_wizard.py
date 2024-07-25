from odoo import models, fields, api

class ChangeState(models.TransientModel):
    _name = 'change.state'

    property_id=fields.Many2one('model.a')
    state=fields.Selection([
        ('draft','Draft'),
        ('pending', 'Pending'),
    ],default='draft')
    reason=fields.Char()

    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state=self.state
            self.property_id.create_history_record('closed',self.state,self.reason)

