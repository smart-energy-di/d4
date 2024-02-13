import os
import requests
import pytest

def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False
    except requests.exceptions.ConnectionError:
        return False


@pytest.fixture(scope='session')
def docker_compose_file(pytestconfig):
    """Get the docker-compose.yml absolute path.
    Override this fixture in your tests if you need a custom location.
    """
    return os.path.join(str(pytestconfig.rootdir), "docker-compose-local.yml")


@pytest.fixture(scope='session')
def docker_services_project_name(pytestconfig):
    return "{{cookiecutter.project_slug}}"


@pytest.fixture(scope='session')
def docker_keycloak(docker_ip, docker_services):
    ## docker_services.start('keycloak')
    public_port = docker_services.port_for("keycloak", 8080)
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url



@pytest.fixture(scope='session')
def docker_keycloak(docker_ip, docker_services):
    # docker_services.start('keycloak')
    public_port = docker_services.port_for("keycloak", 8080)
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_opa(docker_ip, docker_services):
    # docker_services.start('opa')
    public_port = docker_services.port_for("opa", 8181)
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_adapter(docker_ip, docker_services):
    # docker_services.start('adapter')
    public_port = docker_services.port_for("adapter", {{cookiecutter.d4service_adapter_port}})
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_cache(docker_ip, docker_services):
    # docker_services.start('cache')
    public_port = docker_services.port_for("cache", {{cookiecutter.d4service_cache_port}})
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_proxy(docker_ip, docker_services):
    # docker_services.start('proxy')
    public_port = docker_services.port_for("proxy", {{cookiecutter.d4service_proxy_http_port}})
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_spot(docker_ip, docker_services):
    # docker_services.start('spot')
    public_port = docker_services.port_for("spot", {{cookiecutter.d4service_spot_port}})
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope='session')
def docker_ui(docker_ip, docker_services):
    # docker_services.start('ui')
    public_port = docker_services.port_for("ui", {{cookiecutter.d4service_ui_port}})
    url = "http://{docker_ip}:{public_port}".format(**locals())
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url
