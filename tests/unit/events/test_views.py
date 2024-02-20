import pytest
from dateutil.relativedelta import relativedelta
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from tests.factories.users import UserFactory
from tests.factories.events import EventFactory


@pytest.mark.django_db
class TestCreateEvent:
    data = {
        "title": "Bob Party",
        "description": "Bob Party",
        "date": timezone.now() + relativedelta(months=1),
        "location": "Kyiv",
    }

    def test_happy_path_is_ok(self, api_client):
        url = reverse("events-list")
        user = UserFactory()
        api_client.force_authenticate(user=user)
        response = api_client.post(path=url, data=self.data)
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["organizer"]["email"] == user.email

    def test_if_date_in_past_then_raise_exc(self, api_client):
        date = timezone.now() - relativedelta(months=1)
        url = reverse("events-list")
        user = UserFactory()
        api_client.force_authenticate(user=user)
        response = api_client.post(
            path=url,
            data={**self.data, "date": date},
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestListEvent:
    def test_happy_path_is_ok(self, api_client):
        url = reverse("events-list")
        user = UserFactory()
        EventFactory()
        api_client.force_authenticate(user=user)
        response = api_client.get(path=url)
        data = response.json()
        assert len(data) == 1


@pytest.mark.django_db
class TestRetrieveEvent:
    def test_happy_path_is_ok(self, api_client):
        event = EventFactory()
        url = reverse("events-detail", args=[event.id])
        user = UserFactory()
        api_client.force_authenticate(user=user)
        response = api_client.get(path=url)
        data = response.json()
        assert data["id"] == event.id


@pytest.mark.django_db
class TestUpdateEvent:
    data = {
        "title": "Sam Party",
        "description": "Sam Party",
        "date": timezone.now() + relativedelta(months=1),
        "location": "Kyiv",
    }

    def test_happy_path_is_ok(self, api_client):
        user = UserFactory()
        event = EventFactory(organizer=user)
        url = reverse("events-detail", args=[event.id])
        api_client.force_authenticate(user=user)
        response = api_client.patch(path=url, data=self.data)
        data = response.json()
        assert data["description"] == self.data["description"]


@pytest.mark.django_db
class TestDeleteEvent:
    def test_happy_path_is_ok(self, api_client):
        user = UserFactory()
        event = EventFactory(organizer=user)
        url = reverse("events-detail", args=[event.id])
        api_client.force_authenticate(user=user)
        response = api_client.delete(path=url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
