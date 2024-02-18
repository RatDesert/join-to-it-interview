from typing import Any

from rest_framework import serializers

from src.apps.events.models import Event
from src.apps.users.models import User


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class CreateEventSerializer(serializers.ModelSerializer):
    organizer = EventUserSerializer(read_only=True)
    participants = EventUserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data: dict[str, Any]) -> Event:
        validated_data["organizer"] = self.context["user"]
        return super().create(validated_data)


class ListEventSerializer(CreateEventSerializer): ...
