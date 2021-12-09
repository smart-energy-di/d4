import requests
from lxml import html


def test_about_01(docker_spot):
    response = requests.get('http://127.0.0.1:{{cookiecutter.d4service_spot_port}}/about/')
    tree = html.fromstring(response.content)
    assert tree.find(".//title").text == 'About'


def test_keycloak_alice01(docker_spot):
    status = 200
    session = requests.Session()
    url_1 = 'http://127.0.0.1:{{cookiecutter.d4service_spot_port}}/login/'
    resp_1 = session.get(url_1)
    tree = html.fromstring(resp_1.content)
    url_2 = tree.xpath('//form[@id="kc-form-login"]')[0].attrib['action']
    form_data = {'username': 'alice', 'password': 'alice', 'credentialId': ''}
    resp_2 = session.post(url_2, data=form_data)
    tree = html.fromstring(resp_2.content)
    assert len(tree.xpath('.//dd[text()="alice@example.com"]')) == 1
