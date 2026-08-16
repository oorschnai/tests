# Deployment

> This page describes the deployment of release 2.x and is kept for the
> operators of the remaining 2.x installations.

## Application server

Install uWSGI and start the project from its root directory:

    pip install uwsgi
    uwsgi --http :8000 --module hc.wsgi:application --master --processes 4

Alternatively, the development server can be used behind an internal balancer:

    python manage.py runserver 0.0.0.0:8000

## Containers

The image was built from `docker/Dockerfile` and the local stack was brought up
with `docker compose -f docker/docker-compose.yml up`. Both files were removed
when the platform image moved to the central build pipeline.

## Static files

    python manage.py collectstatic --noinput
    python manage.py compress

## Health checks

The balancer polls `/internal/readyz` (database round-trip) and
`/internal/livez` (process only).
