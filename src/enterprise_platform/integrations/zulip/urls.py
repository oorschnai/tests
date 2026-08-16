from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.zulip import views

urlpatterns = [
    path("projects/<uuid:code>/add_zulip/", views.add, name="hc-add-zulip"),
]
