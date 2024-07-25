from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ModelA(models.Model):
    _name = 'model.a'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description='Property'

    name = fields.Char(required=True,translate=True)
    ref = fields.Char(default="New",readonly=1)
    description = fields.Text()
    expected_price = fields.Float(tracking=1)
    active=fields.Boolean(default=True)
    expected_selling_date = fields.Date()
    is_late = fields.Boolean()
    selling_price = fields.Float()
    last_name = fields.Char()
    garden = fields.Boolean()
    diff = fields.Float(digits=(0,10),compute="_compute_diff",readonly=0)
    number_of_beds = fields.Integer(default=2)
    owner_id=fields.Many2one('owner')
    owner_phone=fields.Char(related='owner_id.phone',readonly=0,store=1)
    state=fields.Selection([
        ('draft','Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ],default='draft')
    garden_oreientation = fields.Selection([
        ('a', 'A'),
        ('o', 'O'),
        ('o2', 'O2')
    ] ,default='o2')
    _sql_constraints = [
        ('unique_name_must', 'unique("name")', 'This name must be unique')
    ]
    def action(self):
        pass

    def action_open_change(self):
        action=self.env['ir.actions.actions']._for_xml_id('practice.change_state_action')
        action['context']={'default_property_id':self.id}

        return action
    def check_expected_selling_date(self):
        properties_ids = self.search([])
        print(properties_ids)
        print(self)
        for rec in properties_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late=True

    @api.depends('expected_price', 'selling_price', 'owner_id.name')
    def _compute_diff(self):
        for rec in self:
            print("inside the compute field")
            rec.diff = rec.expected_price - rec.selling_price


    @api.onchange('expected_price')
    def _onchange_price(self):
        for rec in self:
            print("inside the compute field")

            return {
                'warning':{
                    'title':'not cajjjj',
                    'message':"cant do it ",
                    'type':"notification"
                }
            }
    @api.constrains('number_of_beds')
    def check_bedrooms(self):
        for rec in self:
            if rec.number_of_beds == 0:
                raise ValidationError('Number of beds must be greater than 0.')

    def action_draft(self):
        for rec in self:
            self.create_history_record(rec.state, 'draft')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            self.create_history_record(rec.state, 'pending')
            rec.state='pending'

    def action_sold(self):
        for rec in self:
            self.create_history_record(rec.state, 'sold')
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            self.create_history_record(rec.state, 'closed')
            rec.state = 'closed'

    def action_open_related_owner(self):
        action=self.env['ir.actions.actions']._for_xml_id('practice.owner_action')
        view_id=self.env.ref('practice.owner_form_view').id
        action['res_id']=self.owner_id.id
        action['views']=[[view_id,'form']]
        return action
    def action_button(self):
        print(self.env['model.a'].search([
            ('name','!=','asd'),
            # ('', '', ''),
        ]))
        # self.create_history_record( 'old', 'new')
    @api.model_create_multi
    def create(self,vals):
        res=super(ModelA,self).create(vals)
        # res=super(self).create(self,vals)
        if res.ref=='New':
            res.ref=self.env['ir.sequence'].next_by_code('property_sequence')
        print("inside the create method")
        print("self",self)
        print("vals",vals)
        return res
    # @api.model
    # def _search(self,domain,offset=0,limit=None,order=None,access_rights_uid=None):
    #     res = super(ModelA, self)._search(domain,offset=0,limit=None,order=None,access_rights_uid=None)
    #     # res=super(self).create(self,vals)
    #     print("inside the search method")
    #     print("self", self)
    #     print("domain", domain)
    #     return res

    def write(self,vals):
        res = super(ModelA, self).write(vals)
        # res=super(self).create(self,vals)
        print("inside the write method")
        print("self of the write", self)
        print("vals odf the write ", vals)
        return res

    def unlink(self):
        res = super(ModelA, self).unlink()
        # res=super(self).create(self,vals)
        print("inside the delete method")
        print("self of the write", self)
        # print("vals odf the write ", vals)
        return res

    def create_history_record(self,oldState,newState,reason=""):
        for rec in self:
            self.env['property.history'].create({
                'user_id':self.env.uid,
                'property_id':rec.id,
                'old_state':oldState,
                'new_state': newState,
                'reason':reason
            })

