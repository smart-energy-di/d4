import os

import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "docker-compose.yml")

#    return os.path.join(str(pytestconfig.rootdir), "backend", "tests", "docker-compose.yml")
