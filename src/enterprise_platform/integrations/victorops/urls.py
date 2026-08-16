from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.victorops import views

urlpatterns = [
    path("projects/<uuid:code>/add_victorops/", views.add, name="hc-add-victorops"),
]
