import os

import pytest


@pytest.fixture(scope='session')
def docker_compose_files(pytestconfig):
    """Get the docker-compose.yml absolute path.
    Override this fixture in your tests if you need a custom location.
    """
    return [
        os.path.join(str(pytestconfig.rootdir), "docker-compose-local.yml"),
    ]


@pytest.fixture(scope='session')
def docker_services_project_name(pytestconfig):
    return "{{cookiecutter.project_slug}}"


@pytest.fixture(scope='session')
def docker_keycloak(docker_services):
    docker_services.start('keycloak')
    public_port = docker_services.wait_for_service("keycloak", 8080)
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_opa(docker_services):
    docker_services.start('opa')
    public_port = docker_services.wait_for_service("opa", 8181)
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_adapter(docker_services):
    docker_services.start('adapter')
    public_port = docker_services.wait_for_service("adapter", {{cookiecutter.d4service_adapter_port}})
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_cache(docker_services):
    docker_services.start('cache')
    public_port = docker_services.wait_for_service("cache", {{cookiecutter.d4service_cache_port}})
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_proxy(docker_services):
    docker_services.start('proxy')
    public_port = docker_services.wait_for_service("proxy", {{cookiecutter.d4service_proxy_http_port}})
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_spot(docker_services):
    docker_services.start('spot')
    public_port = docker_services.wait_for_service("spot", {{cookiecutter.d4service_spot_port}})
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url


@pytest.fixture(scope='session')
def docker_ui(docker_services):
    docker_services.start('ui')
    public_port = docker_services.wait_for_service("ui", {{cookiecutter.d4service_ui_port}})
    url = "http://{docker_services.docker_ip}:{public_port}".format(**locals())
    return url
