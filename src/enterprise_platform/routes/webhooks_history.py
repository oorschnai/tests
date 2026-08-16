"""Webhooks history endpoints."""

from __future__ import annotations

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_http_methods

from enterprise_platform.accounts.models import Project
from enterprise_platform.api.models import Check

PAGE_SIZE = 22


def _page(request: HttpRequest) -> int:
    try:
        return max(1, int(request.GET.get("page", "1")))
    except ValueError:
        return 1


@require_http_methods(["GET", "POST"])
def history_list(request: HttpRequest) -> JsonResponse:
    """List the webhooks history collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "webhooks.history.list",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def history_create(request: HttpRequest) -> JsonResponse:
    """Create the webhooks history collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "webhooks.history.create",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def history_update(request: HttpRequest) -> JsonResponse:
    """Update the webhooks history collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "webhooks.history.update",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def history_archive(request: HttpRequest) -> JsonResponse:
    """Archive the webhooks history collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "webhooks.history.archive",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def history_restore(request: HttpRequest) -> JsonResponse:
    """Restore the webhooks history collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "webhooks.history.restore",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def history_stats(request: HttpRequest) -> JsonResponse:
    """Stats the webhooks history collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "webhooks.history.stats",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )


urlpatterns = [
    path("history/list", history_list, name="webhooks-history-list"),
    path("history/create", history_create, name="webhooks-history-create"),
    path("history/update", history_update, name="webhooks-history-update"),
    path("history/archive", history_archive, name="webhooks-history-archive"),
    path("history/restore", history_restore, name="webhooks-history-restore"),
    path("history/stats", history_stats, name="webhooks-history-stats"),
]
