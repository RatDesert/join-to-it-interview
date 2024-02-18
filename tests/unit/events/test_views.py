import pytest
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from tests.factories.users import UserFactory


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
