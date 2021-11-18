## let's build acme company

### some information
```bash
$ cookiecutter --version
Cookiecutter 1.7.3 from [...] (Python 3.9)
$ ls -1d acme oceanic-airlines
ls: acme: No such file or directory
ls: oceanic-airlines: No such file or directory
```

# create two example projects

```bash
$ cookiecutter --config-file examples/acme/cookiecutter.yaml --no-input .
$ cookiecutter --config-file examples/oceanic-airlines/cookiecutter.yaml --no-input .
$ ls -1d acme oceanic-airlines
acme
oceanic-airlines
$ cp -av examples/acme/backend/app acme/backend/
examples/acme/backend/app -> acme/backend/app
examples/acme/backend/app/main.py -> acme/backend/app/main.py
$ cp -av examples/oceanic-airlines/backend/app oceanic-airlines/backend/
examples/oceanic-airlines/backend/app -> oceanic-airlines/backend/app
examples/oceanic-airlines/backend/app/main.py -> oceanic-airlines/backend/app/main.py
```

### build and start container

```bash
$ docker-compose -f acme/docker-compose.yml build
[...]
$ docker-compose -f oceanic-airlines/docker-compose.yml build
[...]
$ docker-compose -f acme/docker-compose.yml up -d
Creating network "acme_default" with the default driver
Creating acme_frontend_1 ... done
Creating acme_backend_1  ... done
$ docker-compose -f oceanic-airlines/docker-compose.yml up -d
Creating network "oceanic-airlines_default" with the default driver
Creating volume "oceanic-airlines_app-db-data" with default driver
Creating oceanic-airlines_backend_1  ... done
Creating oceanic-airlines_frontend_1 ... done
$ docker ps
CONTAINER ID   IMAGE               COMMAND       CREATED          STATUS          PORTS                  NAMES
f34ff0c11460   d4backend:latest    "/start.sh"   8 seconds ago    Up 6 seconds    0.0.0.0:9210->80/tcp   oceanic-airlines_backend_1
c36d0e9a59e7   d4frontend:latest   "/start.sh"   8 seconds ago    Up 6 seconds    0.0.0.0:9220->80/tcp   oceanic-airlines_frontend_1
f4d288267335   d4frontend:latest   "/start.sh"   19 seconds ago   Up 18 seconds   0.0.0.0:9120->80/tcp   acme_frontend_1
eb1cfb47aa2b   d4backend:latest    "/start.sh"   19 seconds ago   Up 18 seconds   0.0.0.0:9110->80/tcp   acme_backend_1
```

### check, what is going on

todo

### remove container

```bash
$ docker-compose -f oceanic-airlines/docker-compose.yml down
Stopping oceanic-airlines_backend_1  ... done
Stopping oceanic-airlines_frontend_1 ... done
Removing oceanic-airlines_backend_1  ... done
Removing oceanic-airlines_frontend_1 ... done
Removing network oceanic-airlines_default
$ docker-compose -f acme/docker-compose.yml down
Stopping acme_frontend_1 ... done
Stopping acme_backend_1  ... done
Removing acme_frontend_1 ... done
Removing acme_backend_1  ... done
Removing network acme_default
```
