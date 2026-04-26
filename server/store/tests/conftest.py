import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def client() -> APIClient:
    return APIClient()
