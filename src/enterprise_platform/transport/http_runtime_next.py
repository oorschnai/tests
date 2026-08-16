"""ASGI variant of the serving runtime.

Behind EP_ASGI, not enabled anywhere yet: the notification senders still use
blocking sockets, so the worker threads starve under load.
"""

from __future__ import annotations

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enterprise_platform.settings")

if os.getenv("EP_ASGI") != "1":
    raise RuntimeError("ASGI runtime is not enabled in this environment")

application_v2 = get_asgi_application()
