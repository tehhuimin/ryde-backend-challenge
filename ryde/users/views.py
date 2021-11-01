from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.views import get_schema_view
from .models import Users
from .serializers import UsersSerializer
# from .serializers import UsersSerializer

class ListUsers(APIView):

    def get(self, request, format=None):
        """
        Read data of all users
        """
        try: 
            users = Users.objects.all()
            users_response = UsersSerializer(users, many=True).data
            response = {
                "users": users_response
            }
            return Response(data = response, status=status.HTTP_200_OK)
        except Exception as e: 
            return Response(data={'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, format=None):
        """
        Create a new user
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response(data = {'post': ['hi', 'hi2']}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        """
        Update user
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response(data = {'put': ['hi', 'hi2']}, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        Delete a specific user
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response(data = {'delete': ['hi', 'hi2']}, status=status.HTTP_200_OK)
