import requests

from busca_localidades import BuscaLocalidades


def test_status_code():
    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    req = requests.get(url)
    assert req.status_code == 200


def test_todos_estatos_presentes():
    estados = BuscaLocalidades
    assert len(list(estados.SIGLAS)) == 27
