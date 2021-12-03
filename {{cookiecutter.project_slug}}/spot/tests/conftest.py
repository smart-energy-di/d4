import os

import pytest
import requests


def is_responsive(url):
    try:
        response = requests.get(url)
        # if response.status_code == 200:
        if response.status_code < 500:
            return True
    except ConnectionError:
        return False
    except Exception:
        return False


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "test-spot-docker-compose.yml")
    # return os.path.join(str(pytestconfig.rootdir), "docker-compose.yml")
    # return os.path.join(str(pytestconfig.rootdir), "backend", "tests", "docker-compose.yml")


@pytest.fixture(scope='session')
def docker_keycloak(docker_ip, docker_services):
    public_port = docker_services.port_for("keycloak", 8080)
    url = "http://{}:{}".format(docker_ip, public_port)
    aaa = is_responsive(url)
    # import pdb
    # pdb.set_trace()
    docker_services.wait_until_responsive(
        timeout=100.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_opa(docker_ip, docker_services):
    # import pdb
    # pdb.set_trace()
    public_port = docker_services.port_for("opa", 8181)
    url = "http://{}:{}".format(docker_ip, public_port)
    docker_services.wait_until_responsive(
        timeout=100.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_spot(docker_ip, docker_services):
    # import pdb
    # pdb.set_trace()
    public_port = docker_services.port_for("spot", 80)
    url = "http://{}:{}".format(docker_ip, public_port)
    docker_services.wait_until_responsive(
        timeout=100.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url

# @pytest.fixture(scope="session")
# def keycloak_service(docker_ip, docker_services):
#     """Ensure that HTTP service is up and responsive."""
#
#     # `port_for` takes a container port and returns the corresponding host port
#     port = docker_services.port_for("keycloak", 8080)
#     url = "http://{}:{}".format(docker_ip, port)
#     docker_services.wait_until_responsive(
#         timeout=100.0, pause=0.1, check=lambda: is_responsive(url)
#     )
#     return url
