## Local setup

Poetry >= 1.7.0 should be used. <br />
To install poetry you can run:

```
 curl -sSL https://install.python-poetry.org | python3 -
```

```
poetry shell
```

```
poetry install
```

Create src/settings/local.py <br />
Example: src/settings/local.example.py

## Start application

```
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py runserver
```

## Docs

Visit: \<domain>\/docs <br />
Example:
http://localhost:8000/docs
