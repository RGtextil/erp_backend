from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
<<<<<<< HEAD
          if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Las contraseñas no coinciden"}) 
          validate_password(attrs['password'])
          return attrs

    def create(self, validated_data):
            password = validated_data.pop('password')
            validated_data.pop('password2', None)

            user = User.objects.create_user(password=password, **validated_data)
            return user      
     
=======
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Las contraseñas no coinciden"})
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        # Quitamos password2 porque no existe en el modelo
        validated_data.pop('password2')
>>>>>>> 0c1658b9099aa6ae43392d0bf5877bd3687095e0

        # Extraemos y encriptamos la contraseña
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id', 'email', 'username')

