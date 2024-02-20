import pytest
from src.apps.events.models import Event
from tests.factories.events import EventFactory
from tests.factories.users import UserFactory
from src.apps.events.filters import EventsFilterSet


@pytest.mark.django_db
class TestEventFilterSet:
    def test_organizer_ids_filter_is_ok(self):
        organizer = UserFactory()
        EventFactory(organizer=organizer)
        EventFactory(organizer=organizer)
        EventFactory()
        qs = Event.objects.all()
        f = EventsFilterSet(data={"organizer_ids": f"{organizer.id}"}, queryset=qs)
        assert f.qs.count() == 2

    def test_participant_ids_filter_is_ok(self):
        user_1 = UserFactory()
        user_2 = UserFactory()

        event_1 = EventFactory()
        event_2 = EventFactory()
        EventFactory()

        event_1.add_participant(user_1)
        event_2.add_participant(user_2)
        event_2.add_participant(user_1)

        qs = Event.objects.all()
        f = EventsFilterSet(data={"participant_ids": f"{user_1.id}, {user_2.id}"}, queryset=qs)
        assert f.qs.count() == 2
