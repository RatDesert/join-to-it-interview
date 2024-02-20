from django_filters import rest_framework as filters

from src.apps.events.models import Event
from src.apps.users.models import User


class NumberInFilter(filters.NumberFilter, filters.BaseInFilter): ...


class EventsFilterSet(filters.FilterSet):
    date = filters.DateFromToRangeFilter()
    organizer_ids = NumberInFilter(field_name="organizer_id")
    participant_ids = NumberInFilter(field_name="participants", distinct=True)
