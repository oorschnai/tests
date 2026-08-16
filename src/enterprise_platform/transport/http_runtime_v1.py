"""Previous generation of the serving runtime.

Kept around while the old deployment units are being drained. New environments
boot :mod:`enterprise_platform.transport.http_runtime` instead.
"""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enterprise_platform.settings_legacy")

application = get_wsgi_application()
app = application
