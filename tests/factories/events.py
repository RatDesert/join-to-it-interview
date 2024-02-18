from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from src.apps.events.models import Event
from tests.factories.users import UserFactory


class EventFactory(DjangoModelFactory):
    title = Faker("sentence", nb_words=4)
    description = Faker("text", max_nb_chars=100)
    date = Faker("future_date")
    location = Faker("address")
    organizer = SubFactory(UserFactory)

    class Meta:
        model = Event
