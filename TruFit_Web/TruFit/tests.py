from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import TFUser
import json
import datetime
from django.core.exceptions import ObjectDoesNotExist
from .views import index, user_authentication, add_new_user, modify_user_information, list_users, delete_user


# class UserAuthenticationTest(TestCase):
#
#     def setUp(self):
#         self.client = APIClient()
#         self.url = reverse('user_authentication')
#         self.valid_user = TFUser.objects.create(email='kavin.babu@photon.com', role='admin', active_role='admin')
#         self.valid_payload = {
#             'name': 'kavin babu',
#             'email': 'kavin.babu@photon.com'
#         }
#         self.invalid_payload = {
#             'username': 'kavin babu',
#             'email': 'kajal.v@photon.com'}
#
#     def test_valid_user(self):
#         status_code = 200
#         response = self.client.post(self.url, data=json.dumps(self.valid_payload), content_type='application/json')
#
#         response_data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(response_data['name'], 'kavin babu')
#         self.assertEqual(response_data['email'], 'kavin.babu@photon.com')
#         self.assertEqual(response_data['role'], 'admin')
#         self.assertEqual(response_data['active_role'], 'admin')
#
#     def test_invalid_user(self):
#         response = self.client.post(self.url, data=json.dumps(self.invalid_payload), content_type='application/json')
#         response_data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response_data['error_code'], 'TF1000')
#         self.assertEqual(response_data['err_msg'], 'User not found in the TruFit Application')
#
#
# class DeleteUserTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#         self.email = 'kavin.babu@photon.com'
#         self.user = TFUser.objects.create(name="kavin babu", email=self.email, role='admin', active_role='admin')
#         self.url = reverse('delete_user')
#         self.valid_payload = {
#             #'name': 'kavin babu',
#             'email': 'kavin.babu@photon.com'
#         }
#
#     def test_delete_user(self):
#         #send a get request to delete user
#         response = self.client.post(self.url,data=json.dumps(self.valid_payload), content_type='application/json')
#
#         response_data = response.json()
#         #Assert that the response has a status code 405
#         self.assertEqual(response.status_code, 405)
#         #Assert that the user has been deleted
#         self.assertEqual(list(TFUser.objects.filter(email=self.email)), [])
#         # self.assertEqual(json.loads(response.content),{'Status_msg':'User deleted successfully'} )
#         self.assertEqual(response_data['status_msg'], 'User deleted successfully')
#
#     def test_delete_user_not_exist(self):
#         # send a get request to delete user
#         response = self.client.post(self.url, data=json.dumps(self.valid_payload), content_type='application/json')
#         # import pdb
#         # pdb.set_trace()
#         response_data = response.json()
#         # Assert that the response has a status code 404
#         self.assertEqual(response.status_code, 405)
#         #Assert that the user has been deleted
#         # self.assertEqual(json.loads(response.content), {'error_code': 'TF1003', 'error_msg': 'User not exists'})
#         # self.assertEqual(response_data['error_code'], 'TF1003')
#         # self.assertEqual(response_data['error_msg'], 'User not exists')
#
#
#
# class AddUserTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#         self.email = 'kavin.babu@photon.com'
#         self.user = TFUser.objects.create(name="kavin babu", email=self.email, role='admin', active_role='admin')
#         self.url = reverse('add_new_user')
#         self.payload1= {
#             'username': 'kavin babu',
#             'email': 'kavin.babu@photon.com',
#             'role':'admin'
#         }
#
#         self.payload2 = {
#             'username': 'Kajal Verma',
#             'email': 'kajal.v@photon.com',
#             'role': 'admin'
#         }
#
#     def test_Add_userExist(self):
#         # send a get request to add user
#         response = self.client.post(self.url, data=json.dumps(self.payload1), content_type='application/json')
#         # import pdb
#         # pdb.set_trace()
#         # Assert that the response has a status code 500
#         self.assertEqual(response.status_code, 500)
#         # Assert that the user has been added
#         self.assertEqual(json.loads(response.content), {'error_code': 'TF1001', 'error_msg': 'User already exists'})
#
#     def test_AddUser(self):
#         response = self.client.post(self.url, data=json.dumps(self.payload2), content_type='application/json')
#
#         response_data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # import pdb
#         # pdb.set_trace()
#         #
#         self.assertEqual(response_data['Status_msg'], 'User created successfully')


# class ListUserTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#         # self.email = 'kavin.babu@photon.com'
#         self.user = TFUser.objects.create(email='kajal.v@photon.com',role='admin', active_role='SalesEngineer')
#         self.url = reverse('list_users')
#
#
#         self.payload = {
#             'username': 'Kajal Verma',
#             'email': 'kajal.v@photon.com',
#             'role': 'admin',
#             'active_role': 'SalesEngineer'
#         }
#
# def test_ListUserExist(self): # send a get request to add user response = self.client.post(self.url,
# data=json.dumps(self.payload), content_type='application/json') import pdb pdb.set_trace() # Assert that the user
# has been added self.assertEqual(response.json(), {'user_info': [{'id': 1, 'name': '', 'email':
# 'kajal.v@photon.com', 'role': 'admin', 'active_role': 'SalesEngineer', 'created_date': '2023-01-24T13:27:23.605Z',
# 'modified_date': '2023-01-24T13:29:59.668Z'}]})

class ModifyUserInformation(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = TFUser.objects.create(name='kavin babu', email='kavin.babu@photon.com', role='salesengineer')
        self.url = reverse('modify_user_information')
        self.payload1 = {
            'username': 'kavin babu',
            'email': 'kavin.babu@photon.com',
            'role': 'SalesEngineer'
        }

    def ModifyUserSuccess(self):
        response = self.client.post(self.url, data=json.dumps(self.payload1), content_type='application/json')
        response_data = response.json()
        self.assertEqual(response_data['Status_msg'], 'User modified successfully')

    # def UserServerException(self):
    #     # send a get request to delete user
    #     response = self.client.post(self.url, data=json.dumps(self.valid_payload), content_type='application/json')
    #     # import pdb
    #     # pdb.set_trace()
    #     response_data = response.json()
    #     # Assert that the response has a status code 404
    #     self.assertEqual(response.status_code, 500)
    #     #Assert that the user has been deleted
    #     self.assertEqual(response.data['error_code'],'TF1003')
    #     self.assertEqual(response.data['error_msg'],'Server Exception')


class ModifyUserTestUserTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.email = 'kavin.babu@photon.com'
        self.user = TFUser.objects.create(name='kavin babu', email='kavin.babu@photon.com', role='salesengineer')
        self.url = reverse('modify_user_information')
        self.payload1 = {
            'username': 'kavin babu',
            'email': 'kavin.babu@photon.com',
            'role': 'SalesEngineer'
        }

    def test_modify_user(self):
        # send a get request to delete user
        response = self.client.post(self.url, data=json.dumps(self.payload1), content_type='application/json')
        import pdb
        pdb.set_trace()

        response_data = response.json()
        self.assertEqual(response_data['Status_msg'], 'User modified successfully')
