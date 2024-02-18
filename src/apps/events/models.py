from django.conf import settings
from django.db import models

from src.apps.events.exceptions import UserAlreadyRegisteredForEvent
from src.apps.events.services import send_email_on_registration_for_event
from src.apps.events.validators import validate_event_date
from src.apps.users.models import User


class Event(models.Model):
    title = models.CharField("Title", max_length=128, unique=True)
    description = models.CharField("Description", max_length=1024)
    date = models.DateTimeField("Date", validators=[validate_event_date])
    location = models.CharField("Location", max_length=128)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organizer_in_events"
    )
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="participant_in_events", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def add_participant(self, user: User) -> None:
        if user == self.organizer or user in self.participants.all():
            raise UserAlreadyRegisteredForEvent

        self.participants.add(user)
        send_email_on_registration_for_event(self, user)
