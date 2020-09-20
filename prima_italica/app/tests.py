# Create your tests here.
import pytest
from django.urls import reverse


# from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('app:hello'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
