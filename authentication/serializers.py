from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile 

class RegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    country = serializers.CharField(write_only=True)
    age = serializers.IntegerField(required=False, write_only=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'country', 'age', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        country = validated_data.pop('country')
        age = validated_data.pop('age', None)
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')

        user = User.objects.create_user(password=password, **validated_data) 
        UserProfile.objects.create(user=user, phone=phone, country=country, age=age)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        return user
