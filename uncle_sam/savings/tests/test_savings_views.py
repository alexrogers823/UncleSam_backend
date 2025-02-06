import logging

import pytest

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_saving_object(api_client, saving_payload) -> None:
    #create
    response_create = api_client.post('/savings/', data=saving_payload, format='json')
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['priority'] == 2

    #read
    response_read = api_client.get('/savings/', format='json')
    assert response_read.status_code == 200
    assert response_read.data[0]['priority'] == 2


@pytest.mark.django_db
def test_update_saving_object(api_client, saving_payload) -> None:
    #create
    response_create = api_client.post('/savings/', data=saving_payload, format='json')
    saving_id = response_create.data['id']
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['priority'] == 2

    #update
    saving_payload = {
        "title": "International Trip",
        "priority": 1,
        "current_amount": 2850.00,
        "goal": 6000,
        "goal_date": "2025-10-31"
    }

    response_update = api_client.put(f'/savings/{saving_id}/', data=saving_payload, format='json')
    new_priority = response_update.data['priority']
    logger.info(f'Successfully updated saving with ID {saving_id}')
    logger.info(f'New priority is {new_priority}')
    assert response_update.status_code == 200
    assert response_update.data['priority'] == saving_payload['priority']


@pytest.mark.django_db
def test_delete_saving_object(api_client, saving_payload) -> None:
    #create
    response_create = api_client.post('/savings/', data=saving_payload, format='json')
    saving_id = response_create.data['id']
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['priority'] == 2

    #delete
    response_delete = api_client.delete(f'/savings/{saving_id}/', data=saving_payload, format='json')
    logger.info(f'Deleted saving with ID {saving_id}')
    assert response_delete.status_code == 204