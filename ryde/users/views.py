from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.views import get_schema_view
from .models import Users, Address
from .serializers import UsersSerializer
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
import json

class ListUsersView(APIView):
    def get(self, request, format=None):
        """
        Read all users data
        """
        try: 
            users = Users.objects.all()
            users_response = UsersSerializer(users, many=True).data
            response = {
                "users": users_response, 
                'success': True
            }
            return JsonResponse(data = response, status=status.HTTP_200_OK)
        except Exception as e: 
            return JsonResponse(data={'error': str(e), 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UsersView(APIView):

    def get(self, request, id, format=None):
        """
        Read data of one users
        """
        
        try: 
            user = Users.objects.get(id=id)
            serializer = UsersSerializer(user)
            user_response = serializer.data
            response = {
                "user": user_response,
                'success': True
            }
            return JsonResponse(data = response, status=status.HTTP_200_OK)
        except Users.DoesNotExist: 
            return JsonResponse({'error': 'The user does not exist', 'success': False}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e: 
            return JsonResponse(data={'error': str(e), 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Create a new user", 
        request_body=UsersSerializer
    )
    def post(self, request, id, format=None):
        """
        Create a new user
        """
        try: 
            user = Users.objects.get(id=id)
            return JsonResponse(data = {'error': "User already exists", 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            received_data = json.loads(request.body)

            data = { 
                **received_data, 
                "id": id
            }
            try: 
                # check if data is valid
                serializer = UsersSerializer(data=data)
                if serializer.is_valid(): 
                    # get address to be inserted as an embedded model
                    address = data['address']
                    del data['address']
                    created = Users.objects.create(address=Address(**address), **data)
                    return JsonResponse(data = {'data': UsersSerializer(created).data, 'success': True}, status=status.HTTP_201_CREATED)
                else: 
                    return JsonResponse(data = {'error': serializer.errors, 'success': False}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e: 
                return JsonResponse(data={'error': str(e), 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            return JsonResponse(data={'error': str(e), 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_description="Update an user details", 
        request_body=UsersSerializer
    )
    def put(self, request, id, format=None):
        """
        Update user
        """
        try: 
            user = Users.objects.get(id=id)
            received_data = json.loads(request.body)
            data = { 
                **received_data, 
                "id": id
            }
            # check if data is valid
            serializer = UsersSerializer(data=data)
            if serializer.is_valid(): 
                user.name = data.get('name', '')
                user.description = data.get('description', '')
                user.dob = data.get('dob', '')
                user.address = Address(**data.get("address", {}))
                user.save()
                return JsonResponse(data = {'data': serializer.data, 'success': True}, status=status.HTTP_202_ACCEPTED)
            else: 
                return JsonResponse(data = {'error': serializer.errors, 'success': False}, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist: 
            return JsonResponse({'error': 'The user does not exist','success': False}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e: 
            return JsonResponse(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, id, format=None):
        """
        Delete a specific user
        """
        try: 
            user = Users.objects.get(id=id)
            user.delete()
            return JsonResponse(data = {'success': True}, status=status.HTTP_200_OK)
        except Users.DoesNotExist: 
            return JsonResponse({'error': 'The user does not exist','success': False}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e: 
            return JsonResponse(data={'error': str(e), 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
