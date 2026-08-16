"""Probes the balancer polls. Mounted under the ``internal/`` prefix."""

from __future__ import annotations

from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def readyz(request: HttpRequest) -> HttpResponse:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status": "ready"})


@csrf_exempt
def livez(request: HttpRequest) -> HttpResponse:
    return HttpResponse("ok", content_type="text/plain")


urlpatterns = [
    path("readyz", readyz, name="internal-readyz"),
    path("livez", livez, name="internal-livez"),
]
