from odoo.tests.common import TransactionCase


class TestProperty(TransactionCase):
    def setUp(self,*args,**kwargs):
        super(TestProperty,self).setUp()
        self.property_01_record=self.env['model.a'].create({
            'ref':'PRT1000',
            'name':'property_test',
        })


    def test_01_property_value(self):
        property_id=self.property_01_record
        self.assertRecordValues(property_id,[{
            'ref': 'PRT1000',
            'name': 'property_test',
        }])
