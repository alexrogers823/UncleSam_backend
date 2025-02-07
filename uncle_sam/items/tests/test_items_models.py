import pytest


@pytest.mark.django_db
def test_item_amount(item) -> None:
    assert item.amount == 174.95