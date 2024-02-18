from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_event_date(value: datetime) -> None:
    if value < timezone.now():
        raise ValidationError(
            _("The date of the event must be in a future"),
            params={"value": value},
        )
