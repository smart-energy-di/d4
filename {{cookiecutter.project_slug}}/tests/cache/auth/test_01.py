import requests
from lxml import html


def test_keycloak_alice01(docker_cache):
    status = 200
    session = requests.Session()
    url_1 = 'http://127.0.0.1:{{cookiecutter.d4service_cache_port}}/finance/salary/alice'
    resp_1 = session.get(url_1)
    assert resp_1.status_code == status
    tree = html.fromstring(resp_1.content)
    url_2 = tree.xpath('//form[@id="kc-form-login"]')[0].attrib['action']
    form_data = {'username': 'alice', 'password': 'alice', 'credentialId': ''}
    resp_2 = session.post(url_2, data=form_data)
    assert resp_2.json() == {"msg": "success", "name": "alice"}


def test_keycloak_bob01(docker_cache):
    status = 200
    session = requests.Session()
    url_1 = 'http://127.0.0.1:{{cookiecutter.d4service_cache_port}}/finance/salary/bob'
    resp_1 = session.get(url_1)
    assert resp_1.status_code == status
    tree = html.fromstring(resp_1.content)
    url_2 = tree.xpath('//form[@id="kc-form-login"]')[0].attrib['action']
    form_data = {'username': 'bob', 'password': 'bob', 'credentialId': ''}
    resp_2 = session.post(url_2, data=form_data)
    assert resp_2.json() == {"msg": "success", "name": "bob"}


def test_keycloak_bob02(docker_cache):
    status = 200
    session = requests.Session()
    url_1 = 'http://127.0.0.1:{{cookiecutter.d4service_cache_port}}/finance/salary/alice'
    resp_1 = session.get(url_1)
    assert resp_1.status_code == status
    tree = html.fromstring(resp_1.content)
    url_2 = tree.xpath('//form[@id="kc-form-login"]')[0].attrib['action']
    form_data = {'username': 'bob', 'password': 'bob', 'credentialId': ''}
    resp_2 = session.post(url_2, data=form_data)
    assert resp_2.json() == {"msg": "success", "name": "alice"}
