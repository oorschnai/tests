"""Mounts every route module under its own prefix.

The prefix is the module name with underscores turned into slashes, so
``routes/internal.py`` serves ``/internal/readyz`` and
``routes/billing_invoices.py`` serves ``/billing/invoices/...``.
"""

from __future__ import annotations

import pkgutil

from django.urls import include, path

import enterprise_platform.routes as routes_package

SKIP = {"registry"}


def build() -> list:
    patterns = []
    for module in sorted(
        m.name for m in pkgutil.iter_modules(routes_package.__path__)
    ):
        if module in SKIP:
            continue
        prefix = module.replace("_", "/")
        patterns.append(
            path(f"{prefix}/", include(f"enterprise_platform.routes.{module}"))
        )
    return patterns


urlpatterns = build()
