"""Serving runtime of the platform. This is what Procfile boots."""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application

from enterprise_platform.transport.middleware import ProxyHeaders, RequestTiming

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enterprise_platform.settings")
os.environ.setdefault("EP_RUNTIME", "http")

_django = get_wsgi_application()

application_v2 = ProxyHeaders(RequestTiming(_django))
