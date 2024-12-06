from django.db.models import Count, Q
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'name')

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует")
        return data

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("password должен быть не менее 8 символов")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
        )
        return user



