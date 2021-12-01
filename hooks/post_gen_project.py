import os
import shutil

# print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

enable_adapter = '{{cookiecutter.enable_adapter}}' == 'y'
enable_cache = '{{cookiecutter.enable_cache}}' == 'y'
enable_ui = '{{cookiecutter.enable_ui}}' == 'y'
enable_proxy = '{{cookiecutter.enable_proxy}}' == 'y'
enable_spot = '{{cookiecutter.enable_spot}}' == 'y'


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not enable_adapter:
    remove('./test-adapter-docker-compose.yml')
    remove('./adapter')

if not enable_cache:
    remove('./test-cache-docker-compose.yml')
    remove('./cache')

if not enable_ui:
    remove('./test-ui-docker-compose.yml')
    remove('./ui')

if not enable_proxy:
    remove('./test-proxy-docker-compose.yml')
    remove('./proxy')

if not enable_spot:
    remove('./test-spot-docker-compose.yml')
    remove('./spot')
