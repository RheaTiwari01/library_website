from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','username','email')
class RegisterSerial(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('username','email','password')
    def create(self,valid_data):
        user = User.objects.create_user(
            valid_data['username'],
            valid_data['email'],
            valid_data['password'],
        )
        return user
class LoginSerial(serializers.Serializer):

    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True,write_only=True)
