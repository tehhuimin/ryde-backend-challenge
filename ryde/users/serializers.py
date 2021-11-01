from rest_framework import serializers
from .models import Users, Address

class AddressSerializer(serializers.ModelSerializer):
    address_1 = serializers.CharField(max_length=128)
    address_2 = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=64)
    state = serializers.CharField(max_length=64)
    zip_code = serializers.CharField(max_length=6)

    class Meta: 
        model = Address
        fields = ('address_1', 'address_2', 'city', 'state', 'zip_code')

class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)     # user name
    description = serializers.CharField()
    createdAt = serializers.DateTimeField()
    dob = serializers.DateField()
    id = serializers.PrimaryKeyRelatedField(read_only=True)   # user id
    address = AddressSerializer()

    class Meta: 
        model = Users
        fields = '__all__'
