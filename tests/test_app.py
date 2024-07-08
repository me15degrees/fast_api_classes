from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_html_deve_retornar_ok_e_ola_mundo_html():
    client = TestClient(app)  # arrange (organização)

    response = client.get('/html')  # act (ação)

    assert response.status_code == HTTPStatus.OK  # assert (afirmar)
    assert response.text == '<html><body><h1>Olá Mundo!</h1></body></html>'
