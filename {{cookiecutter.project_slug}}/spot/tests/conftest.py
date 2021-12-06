import os

import pytest


@pytest.fixture(scope='session')
def docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    Override this fixture in your tests if you need a custom location.
    """
    return [
        os.path.join(str(pytestconfig.rootdir), "test-spot-docker-compose.yml"),
    ]


@pytest.fixture(scope='session')
def docker_services_project_name(pytestconfig):
    return "{{cookiecutter.project_slug}}"


@pytest.fixture(scope='session')
def docker_keycloak(docker_services):
    # docker_services.start('keycloak')
    public_port = docker_services.wait_for_service("keycloak", 8080)
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_opa(docker_services):
    # docker_services.start('opa')
    public_port = docker_services.wait_for_service("opa", 8181)
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_spot(docker_services):
    # docker_services.start('spot')
    public_port = docker_services.wait_for_service("spot", 9030)
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url
