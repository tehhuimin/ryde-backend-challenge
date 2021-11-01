from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

class ListUsers(APIView):

    def get(self, request, format=None):
        """
        Read data of a user
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response(data = {'list_of_users': ['hi', 'hi2']}, status=status.HTTP_200_OK)

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
