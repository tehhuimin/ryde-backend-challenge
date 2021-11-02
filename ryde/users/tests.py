from django.test import TestCase, Client
from .models import *
from django.urls import reverse
import json

class GetUsersTest(TestCase):

    def setUp(self):
        """
            Setting up data for tests.
        """
        self.client = Client()

        self.test_address1 = {
                    'address_1' : "tmp", 
                    'address_2': "1",
                    'city' : "",  
                    'zip_code' : "111111", 
                    'state': "test", 
                }
        self.data1 = {
            "id": "test",  
            "name": "test", 
            "description": "test description",
            "dob": "2001-01-01"
        }
        self.test_user1 = Users.objects.create(**self.data1, address=Address(**self.test_address1))

        self.test_address2 = {
                    'address_1' : "70 Newton Road 03-29 Hotel Royal", 
                    'city' : "Singapore",  
                    'zip_code' : "307964", 
                    'state': "Singapore"
                }
        self.data2 = {
            "id": "yahui-wei",  
            "name": "Yahui Wei", 
            "description": "male",
            "dob": "1976-10-20"
        }
        self.test_user2 = Users.objects.create(**self.data2, address=Address(**self.test_address2))

    def test_get_all_users(self):
        """
            Test Case: GET /users/
            Test if API is able to retrieve a list of all users
        """
        response = self.client.get(reverse('all_users'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('users' in response.json())
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(len(response_data['users']), 2)
        users_data = response_data['users']
        
        user_1 = users_data[0]['id']
        if user_1 == self.data1['id']: 
            idx_user1 = 0
            idx_user2 = 1
        else: 
            idx_user1 = 1
            idx_user2 = 0
        
        # check user 1 
        self.assertEqual(users_data[idx_user1]['id'], self.data1['id'])
        self.assertEqual(users_data[idx_user1]['name'], self.data1['name'])
        self.assertEqual(users_data[idx_user1]['description'], self.data1['description'])
        self.assertEqual(users_data[idx_user1]['dob'], self.data1['dob'])
        self.assertTrue('createdAt' in users_data[idx_user1])
        self.assertEqual(users_data[idx_user1]['address'], self.test_address1)

        # check user 2
        self.assertEqual(users_data[idx_user2]['id'], self.data2['id'])
        self.assertEqual(users_data[idx_user2]['name'], self.data2['name'])
        self.assertEqual(users_data[idx_user2]['description'], self.data2['description'])
        self.assertEqual(users_data[idx_user2]['dob'], self.data2['dob'])
        self.assertTrue('createdAt' in users_data[idx_user2])
        self.assertEqual(users_data[idx_user2]['address'], {**self.test_address2, "address_2": ""})

    def tests_get_specific_user_by_id(self):
        """
            Test Case: GET /users/<str:id>/
            Test if API is able to retrieve data of a specific user based on the user's id
        """
        test_user_id = 'yahui-wei'
        response = self.client.get(reverse('users', args=[test_user_id]))

        # check response format
        self.assertEqual(response.status_code, 200)
        self.assertTrue('user' in response.json())
        response_data = response.json()
        self.assertTrue(response_data['success'])
        user_data = response_data['user']
        
        # check user data 
        self.assertEqual(user_data['id'], self.data2['id'])
        self.assertEqual(user_data['name'], self.data2['name'])
        self.assertEqual(user_data['description'], self.data2['description'])
        self.assertEqual(user_data['dob'], self.data2['dob'])
        self.assertTrue('createdAt' in user_data)
        self.assertEqual(user_data['address'], {**self.test_address2, "address_2": ""})
    
    def tests_create_user(self):
        """
            Test Case: POST /user/<str:id>/
            Test if API is able to create a user with correct fields filled up
        """

        test_user_data = {
            "name": "hui min",
            "description": "",
            "dob": "2021-11-02",
            "address": {
                "address_1": "blk 78 ",
                "city": "singapore",
                "state": "singapore",
                "zip_code": "310078"
            }
        }
        test_user_id = 'hm'
        response = self.client.post(reverse('users', args=[test_user_id]), json.dumps(test_user_data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        user_data = response.json()
        
        # check user data 
        self.assertEqual(user_data['id'], test_user_id)
        self.assertEqual(user_data['name'], test_user_data['name'])
        self.assertEqual(user_data['description'], test_user_data['description'])
        self.assertEqual(user_data['dob'], test_user_data['dob'])
        self.assertTrue('createdAt' in user_data)
        self.assertEqual(user_data['address'], {**test_user_data['address'], "address_2": ""})
    
    def tests_delete_user(self):
        """
            Test Case: DELETE /users/<str:id>/
            Test if API is able to delete user given the user's id
        """
        test_user_id = 'yahui-wei'
        response = self.client.delete(reverse('users', args=[test_user_id]))

        # check response format
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        response_data = response.json()
        self.assertTrue(response_data['success'])
        
        # check if user has already been deleted
        response = self.client.get(reverse('users', args=[test_user_id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue('error' in response.json())
        response_data = response.json()
        self.assertFalse(response_data['success'])
        self.assertEqual(response_data['error'], 'The user does not exist')

    def tests_delete_user_user_doesnt_exist(self):
        """
            Test Case: DELETE /users/<str:id>/
            Test if API is able to return 404 if user id is not found
        """
        test_user_id = 'yahui-wei-test'
        response = self.client.delete(reverse('users', args=[test_user_id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue('error' in response.json())
        response_data = response.json()
        self.assertFalse(response_data['success'])
        self.assertEqual(response_data['error'], 'The user does not exist')

