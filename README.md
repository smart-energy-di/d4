# d4 - Base Project Generator

![GitHub](https://img.shields.io/github/license/mleist/d4?color=00998a)
[![build](https://github.com/mleist/d4/actions/workflows/config.yml/badge.svg)](https://github.com/mleist/d4/actions/workflows/config.yml)
![GitHub Repo stars](https://img.shields.io/github/stars/mleist/d4?color=%2300998a&style=flat)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mleist/d4?color=%2300998a&style=flat)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=%2300998a&style=flat)](https://www.python.org/)
![GitHub top language](https://img.shields.io/github/languages/top/mleist/d4?color=%2300998a)
![https://github.com/cookiecutter/cookiecutter](https://img.shields.io/badge/cookiecutter-template-D4AA00.svg?style=flat&logo=cookiecutter&color=%2300998a)


Generate a backend and frontend stack using Python and json-ld, including interactive API documentation.

## How to use it in a virtual python environment.

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
cookiecutter has created a project under _base-project_.

### Now we start - without any further changes - the backend

```bash
$ cd base-project/backend/
$ uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['[...]/base-project/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [50623] using statreload
INFO:     Started server process [50625]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
### From here on, the generated µService runs.

```bash
$ curl http://127.0.0.1:8000
{"message":"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.10"}
```
## More to read

### There is [_documentation_]({{cookiecutter.project_slug}}/docs).

### There is an [_introduction_](./docs/intro.md) to the d4 basics.

> **What is the difference between _introduction_ and _documentation_?**
> 
> The _introduction_ is for clarification of how d4 works, it is not included in the project cookiecutter will have created.
>
> The _documentation_ is part of the project and thus intended for later use in the generated project.
