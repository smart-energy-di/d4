import requests

from requests.exceptions import ConnectionError


def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


def test_status_code(docker_cache):
    status = 200
    url = 'http://127.0.0.1:{{cookiecutter.d4service_cache_port}}/'
    response = requests.get(url)

    assert response.status_code == status
