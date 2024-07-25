from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    price=fields.Float(compute="_compute_price")
    property_id=fields.Many2one('model.a')

    @api.depends('property_id')
    def _compute_price(self):
        for rec in self:
            rec.price=rec.property_id.selling_price