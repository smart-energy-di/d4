# d4 - Base Project Generator

[![build](https://github.com/mleist/d4/actions/workflows/config.yml/badge.svg)](https://github.com/mleist/d4/actions/workflows/config.yml)

Generate a backend and frontend stack using Python and json-ld, including interactive API documentation.

## How to use it

### optionally create a virtual environment like

```bash
$ python3 -m venv ~/.virtualenvs/d4
$ source ~/.virtualenvs/d4/bin/activate[.fish|.csh]
$ pip --version
pip 21.2.4 from [...]/d4/lib/python3.10/site-packages/pip (python 3.10)
```


### Go to the directory where you want to create your project and run:

```bash
$ pip install --upgrade pip
$ pip install -r requirements_dev.txt
# > cookiecutter https://github.com/mleist/cookiecutter-fastapi-json-ld
$ cookiecutter .
project_name [Base Project]:
project_slug [base-project]:
```

# See more

see documentation [here]({{cookiecutter.project_slug}}/docs)
