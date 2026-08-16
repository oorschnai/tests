from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.msteamsw import views

urlpatterns = [
    path("projects/<uuid:code>/add_msteams/", views.add_msteams, name="hc-add-msteams"),
]
