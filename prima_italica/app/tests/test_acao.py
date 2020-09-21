# Create your tests here.
import pytest
from django.urls import reverse


# from pypro.django_assertions import assert_contains


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_acao_list(api_client):
    url = reverse('app:acao-list')
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.parametrize(
    'nome_acao, instituicao_organizadora, endereco, bairro, cidade, descricao, status_code', [
        ('', '', '', '', '', '', 400),
        ('acao_1', 'instituicao_organizacao_1', 'endereco_1', 'bairro_1', 'cidade_1', 'descricao_1', 201),
        ('acao_2_asdfasdfasdfasdfasdfasdf',
         'instituicao_organizacao_2_asdff',
         'endereco_2_asdfasdfasdfasdfasdf',
         'bairro_2_asdfasdfsadfasdfasdfas',
         'cidade_2_asdfasdfasdfasdfasdfas',
         'descricao_1',
         400),
    ]
)
@pytest.mark.django_db
def test_acao_create(
        nome_acao,
        instituicao_organizadora,
        endereco,
        bairro,
        cidade,
        descricao,
        status_code,
        api_client
):
    url = reverse('app:acao-list')
    data = {
        'nome_acao': nome_acao,
        'instituicao_organizadora': instituicao_organizadora,
        'endereco': endereco,
        'bairro': bairro,
        'cidade': cidade,
        'descricao': descricao,
    }
    response = api_client.post(url, data=data)
    assert response.status_code == status_code