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
    remove('./adapter')
    remove('./tests/adapter')
    remove('./compose/local/adapter')

if not enable_cache:
    remove('./cache')
    remove('./tests/cache')
    remove('./compose/local/cache')

if not enable_ui:
    remove('./ui')
    remove('./tests/ui')
    remove('./compose/local/ui')

if not enable_proxy:
    remove('./proxy')
    remove('./tests/proxy')
    remove('./compose/local/proxy')

if not enable_spot:
    remove('./spot')
    remove('./tests/spot')
    remove('./compose/local/spot')
