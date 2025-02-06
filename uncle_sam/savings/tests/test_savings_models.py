import pytest


@pytest.mark.django_db
def test_saving_priority(saving) -> None:
    assert saving.priority == 2


@pytest.mark.django_db
def test_saving_goal_date_can_be_null(saving) -> None:
    saving.goal_date = None
    assert saving.goal_date == None