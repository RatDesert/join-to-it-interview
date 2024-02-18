import pytest
from rest_framework.test import APIClient
from unittest.mock import patch
from typing import Iterator


@pytest.fixture
def api_client():
    return APIClient()
