import logging

import pytest

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_debt_object(api_client, debt_payload) -> None:
    #create
    response_create = api_client.post('/debts/', data=debt_payload, format='json')
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['title'] == debt_payload['title']

    #read
    response_read = api_client.get('/debts/', format='json')
    assert response_read.status_code == 200
    assert response_read.data[0]['title'] == debt_payload['title']


@pytest.mark.django_db
def test_update_debt_object(api_client, debt_payload) -> None:
    #create
    response_create = api_client.post('/debts/', data=debt_payload, format='json')
    debt_id = response_create.data["id"]
    logger.info(f'Successfully created debt with ID {debt_id}')
    assert response_create.status_code == 201
    assert response_create.data['title'] == debt_payload['title']

    #update
    debt_payload = {
        "title": "Valentine's Day Tax",
        "amount": 46.85,
        "due_date": "2025-02-14"
    }

    response_update = api_client.put(f'/debts/{debt_id}/', data=debt_payload, format='json')
    new_title = response_update.data['title']
    logger.info(f'Successfully updated debt with ID {debt_id}')
    logger.info(f'New title is {new_title}')
    assert response_update.status_code == 200
    assert response_update.data['title'] == debt_payload['title']


@pytest.mark.django_db
def test_delete_debt_object(api_client, debt_payload) -> None:
    #create
    response_create = api_client.post('/debts/', data=debt_payload, format='json')
    debt_id = response_create.data["id"]
    logger.info(f'Successfully created debt with ID {debt_id}')
    assert response_create.status_code == 201
    assert response_create.data['title'] == debt_payload['title']

    #delete
    response_delete = api_client.delete(f'/debts/{debt_id}/', data=debt_payload, format='json')
    logger.info(f'Deleted debt with ID {debt_id}')
    assert response_delete.status_code == 204

