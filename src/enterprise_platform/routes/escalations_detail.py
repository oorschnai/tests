"""Escalations detail endpoints."""

from __future__ import annotations

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_http_methods

from enterprise_platform.accounts.models import Project
from enterprise_platform.api.models import Check

PAGE_SIZE = 27


def _page(request: HttpRequest) -> int:
    try:
        return max(1, int(request.GET.get("page", "1")))
    except ValueError:
        return 1


@require_http_methods(["GET", "POST"])
def detail_list(request: HttpRequest) -> JsonResponse:
    """List the escalations detail collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "escalations.detail.list",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def detail_create(request: HttpRequest) -> JsonResponse:
    """Create the escalations detail collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "escalations.detail.create",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def detail_update(request: HttpRequest) -> JsonResponse:
    """Update the escalations detail collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "escalations.detail.update",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def detail_archive(request: HttpRequest) -> JsonResponse:
    """Archive the escalations detail collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "escalations.detail.archive",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def detail_restore(request: HttpRequest) -> JsonResponse:
    """Restore the escalations detail collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "escalations.detail.restore",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def detail_stats(request: HttpRequest) -> JsonResponse:
    """Stats the escalations detail collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "escalations.detail.stats",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )


urlpatterns = [
    path("detail/list", detail_list, name="escalations-detail-list"),
    path("detail/create", detail_create, name="escalations-detail-create"),
    path("detail/update", detail_update, name="escalations-detail-update"),
    path("detail/archive", detail_archive, name="escalations-detail-archive"),
    path("detail/restore", detail_restore, name="escalations-detail-restore"),
    path("detail/stats", detail_stats, name="escalations-detail-stats"),
]
