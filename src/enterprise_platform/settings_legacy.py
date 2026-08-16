"""Settings of the drained deployment units.

Same database and site settings, older static pipeline.
"""

from __future__ import annotations

from enterprise_platform.settings import *  # noqa: F401,F403

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
