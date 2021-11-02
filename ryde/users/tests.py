from django.test import TestCase, Client
from .models import *
from django.urls import reverse

class GetUsersTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_address = {
                    'address_1' : "tmp", 
                    'address_2': "1",
                    'city' : "",  
                    'zip_code' : "111111", 
                    'state': "test", 
                }
        self.data = {
            "id": "test",  
            "name": "test", 
            "description": "test description",
            "dob": "2001-01-01"
        }
        self.test_user = Users.objects.create(**self.data, address=Address(**self.test_address))

    def test_get_all_users(self):
        response = self.client.get(reverse('all_users'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('users' in response.data)
        self.assertEqual(response.data['users'][0]['id'], self.data['id'])
        self.assertEqual(response.data['users'][0]['name'], self.data['name'])
        self.assertEqual(response.data['users'][0]['description'], self.data['description'])
        self.assertEqual(response.data['users'][0]['dob'], self.data['dob'])
        self.assertTrue('createdAt' in response.data['users'][0])
        self.assertEqual(response.data['users'][0]['address'], self.test_address)
