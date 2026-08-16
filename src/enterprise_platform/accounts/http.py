from __future__ import annotations

from django.contrib.auth.models import User
from django.http import HttpRequest

from enterprise_platform.accounts.models import Profile


class AuthenticatedHttpRequest(HttpRequest):
    user: User
    profile: Profile
