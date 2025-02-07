from datetime import date

import pytest
from items.models import Item
from rest_framework.test import APIClient


@pytest.fixture
def item() -> Item:
    return Item.objects.create(
        created = date(2025, 3, 1),
        title = 'Bowling Ball',
        amount = 174.95,
        completed = False,
        url_link = 'https://github.com/alexrogers823'
    )


@pytest.fixture
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture
def item_payload() -> dict:
    return {
        "title": "Bowling Ball",
        "amount": 174.95,
        "completed": False,
        "url_link": "https://github.com/alexrogers823"
    }