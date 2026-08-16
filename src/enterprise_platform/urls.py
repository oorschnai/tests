from __future__ import annotations

from urllib.parse import urlparse

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from enterprise_platform.accounts import views as accounts_views

prefix = ""
if _path := urlparse(settings.SITE_ROOT).path.lstrip("/"):
    prefix = f"{_path}/"

urlpatterns = [
    path(prefix, include("enterprise_platform.routes.registry")),
    path(f"{prefix}admin/login/", accounts_views.login),
    path(f"{prefix}admin/", admin.site.urls),
    path(prefix, include("enterprise_platform.accounts.urls")),
    path(prefix, include("enterprise_platform.api.urls")),
    path(prefix, include("enterprise_platform.front.urls")),
    path(prefix, include("enterprise_platform.payments.urls")),
    path(prefix, include("enterprise_platform.integrations.apprise.urls")),
    path(prefix, include("enterprise_platform.integrations.call.urls")),
    path(prefix, include("enterprise_platform.integrations.discord.urls")),
    path(prefix, include("enterprise_platform.integrations.email.urls")),
    path(prefix, include("enterprise_platform.integrations.github.urls")),
    path(prefix, include("enterprise_platform.integrations.googlechat.urls")),
    path(prefix, include("enterprise_platform.integrations.gotify.urls")),
    path(prefix, include("enterprise_platform.integrations.group.urls")),
    path(prefix, include("enterprise_platform.integrations.matrix.urls")),
    path(prefix, include("enterprise_platform.integrations.mattermost.urls")),
    path(prefix, include("enterprise_platform.integrations.msteamsw.urls")),
    path(prefix, include("enterprise_platform.integrations.ntfy.urls")),
    path(prefix, include("enterprise_platform.integrations.opsgenie.urls")),
    path(prefix, include("enterprise_platform.integrations.pagertree.urls")),
    path(prefix, include("enterprise_platform.integrations.pd.urls")),
    path(prefix, include("enterprise_platform.integrations.po.urls")),
    path(prefix, include("enterprise_platform.integrations.prometheus.urls")),
    path(prefix, include("enterprise_platform.integrations.pushbullet.urls")),
    path(prefix, include("enterprise_platform.integrations.rocketchat.urls")),
    path(prefix, include("enterprise_platform.integrations.shell.urls")),
    path(prefix, include("enterprise_platform.integrations.signal.urls")),
    path(prefix, include("enterprise_platform.integrations.slack.urls")),
    path(prefix, include("enterprise_platform.integrations.sms.urls")),
    path(prefix, include("enterprise_platform.integrations.spike.urls")),
    path(prefix, include("enterprise_platform.integrations.telegram.urls")),
    path(prefix, include("enterprise_platform.integrations.trello.urls")),
    path(prefix, include("enterprise_platform.integrations.victorops.urls")),
    path(prefix, include("enterprise_platform.integrations.webhook.urls")),
    path(prefix, include("enterprise_platform.integrations.whatsapp.urls")),
    path(prefix, include("enterprise_platform.integrations.zulip.urls")),
]
