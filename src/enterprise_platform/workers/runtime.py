"""Background task runtime.

Runs in the same Python root as the web runtime. Outside of the staging
sandbox the periodic jobs are still driven by the `sendalerts` management
command from cron, so this app is imported by the web process only to register
task signatures.
"""

from __future__ import annotations

import os

import django
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enterprise_platform.settings")
django.setup()

celery_runtime = Celery("enterprise_platform")
celery_runtime.config_from_object("django.conf:settings", namespace="CELERY")
celery_runtime.autodiscover_tasks()


@celery_runtime.task(name="enterprise_platform.workers.ping")
def ping() -> str:
    return "pong"
