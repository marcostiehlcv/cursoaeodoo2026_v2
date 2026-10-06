from odoo.tests import common

class TestEstateProperty(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.estate_property = self.env['estate.property']
        self.estate_owner = self.env['estate.owner']
        self.estate_property_type = self.env['estate.property.type']

        self.property_1 = self.estate_property.create({
            'name': 'Property 1',
            'property_type_id': self.estate_property_type.create({'name': 'Apartment', 'code': 'apartment'}).id,
            'expected_price': 100000,
            'selling_price': 120000,
            'available': True,
            'agent_id': self.env.user.id,
            'owner_id': self.estate_owner.create({'name': 'John Doe'}).id,
        })