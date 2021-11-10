### first tests
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

```bash
$ curl http://127.0.0.1:8000
{"message":"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.10"}
```
