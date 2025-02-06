from datetime import date

import pytest
from debts.models import Debt
from rest_framework.test import APIClient


@pytest.fixture
def debt() -> Debt:
    return Debt.objects.create(
        created = date(2025, 3, 17),
        updated = date(2025, 3, 17),
        title = 'St. Patricks Day Tax',
        amount = 45.32,
        due_date = date(2025, 6, 1)
    )


@pytest.fixture
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture
def debt_payload() -> dict:
    return {
        "title": "St. Patricks Day Tax",
        "amount": 45.32,
        "due_date": "2025-06-01"
    }