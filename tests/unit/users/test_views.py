from uuid import uuid4

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestUserRegistration:
    data = {"first_name": "Bob", "last_name": "Li", "email": "bob@li.com", "password": str(uuid4())}

    def test_happy_path_is_ok(self, api_client):
        url = reverse("users-list")
        response = api_client.post(path=url, data=self.data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_email_exists_then_400(self, api_client):
        url = reverse("users-list")
        api_client.post(path=url, data=self.data)
        response = api_client.post(path=url, data=self.data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
