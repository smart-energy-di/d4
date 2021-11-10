### first docker-compose tests
```bash
$ cookiecutter .
project_name [Base Project]:
project_slug [base-project]:
docker_image_prefix [d4]:
docker_image_backend [d4backend]:
docker_image_frontend [d4frontend]:
```

```bash
$ cd base-project
$ docker-compose up -d
Creating network "base-project_default" with the default driver
Creating base-project_backend_1  ... done
Creating base-project_frontend_1 ... done
```

```bash
$ curl http://127.0.0.1:9010
{"message":"Backend: Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.9"}
$ curl http://127.0.0.1:9020
{"message":"Frontend: Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.9"}
```
