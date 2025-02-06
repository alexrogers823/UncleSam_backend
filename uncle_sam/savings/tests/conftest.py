from datetime import date

import pytest
from rest_framework.test import APIClient
from savings.models import Saving


@pytest.fixture
def saving() -> Saving:
    return Saving.objects.create(
        created = date(2025, 2, 6),
        updated = date(2025, 4, 22),
        title = 'International Trip',
        priority = 2,
        current_amount = 1554.00,
        goal = 6000,
        goal_date = date(2025, 10, 31)
    )


@pytest.fixture
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture
def saving_payload() -> dict:
    return {
        "title": "International Trip",
        "priority": 2,
        "current_amount": 1554.00,
        "goal": 6000,
        "goal_date": "2025-10-31"
    }