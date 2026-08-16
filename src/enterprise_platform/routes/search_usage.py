"""Search usage endpoints."""

from __future__ import annotations

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_http_methods

from enterprise_platform.accounts.models import Project
from enterprise_platform.api.models import Check

PAGE_SIZE = 43


def _page(request: HttpRequest) -> int:
    try:
        return max(1, int(request.GET.get("page", "1")))
    except ValueError:
        return 1


@require_http_methods(["GET", "POST"])
def usage_list(request: HttpRequest) -> JsonResponse:
    """List the search usage collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "search.usage.list",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def usage_create(request: HttpRequest) -> JsonResponse:
    """Create the search usage collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "search.usage.create",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def usage_update(request: HttpRequest) -> JsonResponse:
    """Update the search usage collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "search.usage.update",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def usage_archive(request: HttpRequest) -> JsonResponse:
    """Archive the search usage collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "search.usage.archive",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def usage_restore(request: HttpRequest) -> JsonResponse:
    """Restore the search usage collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "search.usage.restore",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )

@require_http_methods(["GET", "POST"])
def usage_stats(request: HttpRequest) -> JsonResponse:
    """Stats the search usage collection."""
    page = _page(request)
    offset = (page - 1) * PAGE_SIZE
    checks = Check.objects.filter(project__in=Project.objects.all())[
        offset : offset + PAGE_SIZE
    ]
    return JsonResponse(
        {
            "kind": "search.usage.stats",
            "page": page,
            "items": [{"code": str(c.code), "status": c.status} for c in checks],
        }
    )


urlpatterns = [
    path("usage/list", usage_list, name="search-usage-list"),
    path("usage/create", usage_create, name="search-usage-create"),
    path("usage/update", usage_update, name="search-usage-update"),
    path("usage/archive", usage_archive, name="search-usage-archive"),
    path("usage/restore", usage_restore, name="search-usage-restore"),
    path("usage/stats", usage_stats, name="search-usage-stats"),
]
