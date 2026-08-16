"""Exports settings endpoints."""

from __future__ import annotations

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_http_methods

from enterprise_platform.accounts.models import Project
from enterprise_platform.api.models import Check

PAGE_SIZE = 29


def _page(request: HttpRequest) -> int:
    try:
        return max(1, int(request.GET.get("page", "1")))
    except ValueError:
        return 1


@require_http_methods(["GET", "POST"])
def settings_list(request: HttpRequest) -> JsonResponse:
    """List the exports settings collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "exports.settings.list",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def settings_create(request: HttpRequest) -> JsonResponse:
    """Create the exports settings collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "exports.settings.create",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def settings_update(request: HttpRequest) -> JsonResponse:
    """Update the exports settings collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "exports.settings.update",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def settings_archive(request: HttpRequest) -> JsonResponse:
    """Archive the exports settings collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "exports.settings.archive",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def settings_restore(request: HttpRequest) -> JsonResponse:
    """Restore the exports settings collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "exports.settings.restore",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def settings_stats(request: HttpRequest) -> JsonResponse:
    """Stats the exports settings collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "exports.settings.stats",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )


urlpatterns = [
    path("settings/list", settings_list, name="exports-settings-list"),
    path("settings/create", settings_create, name="exports-settings-create"),
    path("settings/update", settings_update, name="exports-settings-update"),
    path("settings/archive", settings_archive, name="exports-settings-archive"),
    path("settings/restore", settings_restore, name="exports-settings-restore"),
    path("settings/stats", settings_stats, name="exports-settings-stats"),
]
