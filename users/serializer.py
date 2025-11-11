from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
      model = User
      fields = ('id', 'email', 'username','phone', 'password', 'password2')

    def validate(self, attrs):
          if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Las contraseñas no coinciden"}) 
          validate_password(attrs['password'])
          return attrs

    def create(self, validated_data):
            password = validated_data.pop('password')
            validated_data.pop('password2', None)

            user = User.objects.create_user(password=password, **validated_data)
            return user      
     

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'email', 'username')

