from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from src.apps.users.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 16}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
