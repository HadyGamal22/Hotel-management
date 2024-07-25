from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    property_id=fields.Many2one('model.a')
    def action_confirm(self):
        res=super(SaleOrder,self).action_confirm()
        # res=super(self).create(self,vals)
        print("onside action confirm")
        print("self",self)
        # print("vals",vals)
        return res