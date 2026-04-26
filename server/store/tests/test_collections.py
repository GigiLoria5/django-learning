from collections.abc import Callable
from typing import Any

import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from core.models import User
from store.models import Collection


@pytest.fixture
def create_collection(api_client: APIClient) -> Callable[..., Any]:
    def do_create_collection(title: str) -> Any:
        return api_client.post("/store/collections/", {"title": title})

    return do_create_collection


@pytest.fixture
def authenticate(api_client: APIClient) -> Callable[..., None]:
    def do_authenticate(is_staff: bool = False):
        api_client.force_authenticate(user=(User(is_staff=is_staff)))

    return do_authenticate


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(
        self, create_collection: Callable[..., Any]
    ) -> None:
        response = create_collection("a")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(
        self,
        create_collection: Callable[..., Any],
        authenticate: Callable[..., None],
    ) -> None:
        authenticate()

        response = create_collection("a")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(
        self,
        create_collection: Callable[..., Any],
        authenticate: Callable[..., None],
    ) -> None:
        authenticate(is_staff=True)

        response = create_collection("")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "title" in response.data

    def test_if_data_is_valid_returns_201(
        self,
        create_collection: Callable[..., Any],
        authenticate: Callable[..., None],
    ) -> None:
        authenticate(is_staff=True)

        response = create_collection("a")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client: APIClient) -> None:
        collection = baker.make(Collection)

        response = api_client.get(f"/store/collections/{collection.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": collection.id,
            "title": collection.title,
            "products_count": 0,
        }
