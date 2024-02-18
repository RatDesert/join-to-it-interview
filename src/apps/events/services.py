from src.apps.users.models import User
from django.core.mail import send_mail
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.apps.events.models import Event


def send_email_on_registration_for_event(event: "Event", user: User):
    return send_mail(
        "Successful registration for the event",
        message=f"Thank you for registering for {event.title}. Date of the event: {event.date}.",
        from_email=None,
        recipient_list=[user.email],
    )
