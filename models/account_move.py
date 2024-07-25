from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'
    def action_do(self):
        # res=super(SaleOrder,self).action_confirm()
        # res=super(self).create(self,vals)
        print(self,"onside action confirm")
        # print("self",self)
        # print("vals",vals)
        # return res