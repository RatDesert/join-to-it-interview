import pytest
from tests.factories.events import EventFactory
from tests.factories.users import UserFactory
from src.apps.events.exceptions import UserAlreadyRegisteredForEvent


@pytest.mark.django_db
class TestEventAddParticipant:
    def test_if_user_successfully_registered_then_send_an_email(self, mailoutbox):
        user = UserFactory()
        event = EventFactory()
        event.add_participant(user)
        assert len(mailoutbox) == 1

    def test_if_user_already_registered_and_tries_to_register_then_raise_exc(self):
        user = UserFactory()
        event = EventFactory()
        event.add_participant(user)
        with pytest.raises(UserAlreadyRegisteredForEvent):
            event.add_participant(user)

    def test_if_organizer_tries_to_register_then_raise_exc(self):
        user = UserFactory()
        event = EventFactory(organizer=user)
        with pytest.raises(UserAlreadyRegisteredForEvent):
            event.add_participant(user)
