# d4 - Base Project Generator

![GitHub](https://img.shields.io/github/license/mleist/d4?color=00998a)
[![build](https://github.com/mleist/d4/actions/workflows/config.yml/badge.svg)](https://github.com/mleist/d4/actions/workflows/config.yml)
[![PyLint](https://github.com/mleist/d4/actions/workflows/lint.yml/badge.svg)](https://github.com/mleist/d4/actions/workflows/lint.yml)
[![GitHub Repo stars](https://img.shields.io/github/stars/mleist/d4?color=%2300998a&style=flat)](https://github.com/mleist/d4/stargazers)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mleist/d4?color=%2300998a&style=flat)](https://github.com/mleist/d4/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=%2300998a&style=flat)](https://www.python.org/)
[![GitHub top language](https://img.shields.io/github/languages/top/mleist/d4?color=%2300998a)](https://github.com/mleist/d4/search?l=python)
![https://github.com/cookiecutter/cookiecutter](https://img.shields.io/badge/cookiecutter-template-D4AA00.svg?style=flat&logo=cookiecutter&color=%2300998a)


Generate a backend and frontend stack using Python and json-ld, including interactive API documentation.

## d4? What is d4 for?

d4 is a kind of template project for creating µServices based on python.
These µServices collect existing data (e.g. inventory data from IT systems) and make this data available
in a distributed way via standardised interfaces (REST-API) and in a standardised form (JSON-LD).

For this purpose, the µServices collect data from several Single Points of Truth ([SPOTs](https://en.wikipedia.org/wiki/Single_source_of_truth))
and offer possibilities to link the individual data sets (from different SPOTs) with each other.
There is also a µService template that can be used to create a very simple SPOT with a web UI and CSV/Excel interface.
This is used for data enrichment (distributed in several locations) that cannot be automatically read from systems.
The templates produce µServices that are intended to enable the value-added consolidation of distributed data across
organisational and departmental boundaries. 

### Some feature aspects:

- µservices adapting and caching [SPOTs](https://en.wikipedia.org/wiki/Single_source_of_truth)
- robust and fast, based on [python](https://www.python.org/), [fastapi](https://fastapi.tiangolo.com/), [docker](https://www.docker.com/)
- uses [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification) (formerly Swagger)
- uses [JSON-LD](https://www.w3.org/TR/json-ld/) including schemas
- a µService can enrich information from its "neighbourhood" itself
- at a "psydocentral" location, a lot of data from µServices can be consolidated in a "big graph DB".
- the template project evolved from various iterations to improve heterogeneous IT infrastructures with "data driven" aspects.


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
