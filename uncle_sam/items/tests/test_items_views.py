import logging

import pytest

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_item(api_client, item_payload) -> None:
    #create
    response_create = api_client.post('/items/', data=item_payload, format='json')
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['amount'] == '174.95'

    #read
    response_read = api_client.get('/items/', format='json')
    assert response_read.status_code == 200
    assert response_read.data[0]['amount'] == '174.95'


@pytest.mark.django_db
def test_update_item(api_client, item_payload) -> None:
    #create
    response_create = api_client.post('/items/', data=item_payload, format='json')
    item_id = response_create.data['id']
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['amount'] == '174.95'

    #update
    item_payload = {
        "title": "Bowling Ball",
        "amount": '174.95',
        "completed": True,
        "url_link": "https://github.com/alexrogers823"
    }

    response_update = api_client.put(f'/items/{item_id}/', data=item_payload, format='json')
    new_completion = response_update.data['completed']
    logger.info(f'Successfully updated item with ID {item_id}')
    logger.info(f'Completed is now {new_completion}')
    assert response_update.status_code == 200
    assert response_update.data['completed'] == item_payload['completed']


@pytest.mark.django_db
def test_delete_item(api_client, item_payload) -> None:
    #create
    response_create = api_client.post('/items/', data=item_payload, format='json')
    item_id = response_create.data['id']
    logger.info(f'{response_create.data}')
    assert response_create.status_code == 201
    assert response_create.data['amount'] == '174.95'

    #delete
    response_delete = api_client.delete(f'/items/{item_id}/', data=item_payload, format='json')
    logger.info(f'Deleted item with ID {item_id}')
    assert response_delete.status_code == 204
