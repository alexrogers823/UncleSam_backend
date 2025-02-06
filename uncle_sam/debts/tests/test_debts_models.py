import pytest
from django.core.exceptions import ValidationError


@pytest.mark.unit
def test_hello_world():
   assert "hello_world" == "hello_world"


@pytest.mark.django_db
def test_debt_title(debt) -> None:
   assert debt.title == 'St. Patricks Day Tax'


# @pytest.mark.django_db
# def test_debt_title_cannot_be_null(debt) -> None:
#    debt.title = None
   
#    with pytest.raises(ValidationError) as e:
#        debt.full_clean()
   
#    assert 'Ensure that title is not null' in str(e.value)



@pytest.mark.django_db
def test_debt_due_date_can_be_null(debt) -> None:
   debt.due_date = None
   assert debt.due_date == None #?