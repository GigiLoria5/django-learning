import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCreateCollection:
    BASE_URL = "/store/collections/"

    def test_if_user_is_anonymous_returns_401(self, client: APIClient) -> None:
        response = client.post(self.BASE_URL, {"title": "Test Collection"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
