### first docker-compose tests
```bash
$ cookiecutter .
project_name [Base Project]:
project_slug [base-project]:
docker_image_prefix []:
docker_image_backend [backend]:
docker_image_frontend [frontend]:
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
```
