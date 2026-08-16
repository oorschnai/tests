from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.ntfy import views

urlpatterns = [
    path("projects/<uuid:code>/add_ntfy/", views.add, name="hc-add-ntfy"),
]
