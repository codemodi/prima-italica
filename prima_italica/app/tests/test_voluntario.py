# Create your tests here.
import pytest
from django.urls import reverse


# from pypro.django_assertions import assert_contains


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_voluntario_list(api_client):
    url = reverse('app:voluntario-list')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize(
    'nome, sobrenome, bairro, cidade, status_code', [
        ('', '', '', '', 400),
        ('nome_1', 'sobrenome_1', 'bairro_1', 'cidade_1', 201),
        ('nome_2_asdfasdfasdfasdfasdfasdf',
         'sobrenome_2_asdffasdfasdfasdfds',
         'bairro_2_asdfasdfsadfasdfasdfas',
         'cidade_2_asdfasdfasdfasdfasdfas',
         400),
    ]
)
@pytest.mark.django_db
def test_voluntario_create(
        nome,
        sobrenome,
        bairro,
        cidade,
        status_code,
        api_client
):
    url = reverse('app:voluntario-list')
    data = {
        'nome': nome,
        'sobrenome': sobrenome,
        'bairro': bairro,
        'cidade': cidade,
    }
    response = api_client.post(url, data=data, format='json')
    assert response.status_code == status_code
