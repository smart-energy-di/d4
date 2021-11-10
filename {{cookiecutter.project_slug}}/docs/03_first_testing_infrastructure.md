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
$ pip install -r backend/requirements_dev.txt
[...]
```

```bash
$ pytest .
====================================================== test session starts =======================================================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/markus/Git_Reps/d4/base-project
plugins: docker-0.10.3
collected 1 item

backend/tests/test_my_first.py .                                                                                           [100%]

======================================================= 1 passed in 8.59s ========================================================
```

This results in a quite simple test whether a GET request on "/" returns a response with code 200.

```python
...
def test_status_code(http_service):
    status = 200
    response = requests.get(http_service + "/")

    assert response.status_code == status
...
```
