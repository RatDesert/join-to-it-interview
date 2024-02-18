from django.utils import timezone
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from src.apps.events.models import Event
from tests.factories.users import UserFactory


class EventFactory(DjangoModelFactory):
    title = Faker("sentence", nb_words=4)
    description = Faker("text", max_nb_chars=100)
    date = Faker("future_datetime", tzinfo=timezone.get_current_timezone())
    location = Faker("address")
    organizer = SubFactory(UserFactory)

    class Meta:
        model = Event
