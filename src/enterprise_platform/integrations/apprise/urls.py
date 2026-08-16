from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.apprise import views

urlpatterns = [
    path("projects/<uuid:code>/add_apprise/", views.add, name="hc-add-apprise"),
]
