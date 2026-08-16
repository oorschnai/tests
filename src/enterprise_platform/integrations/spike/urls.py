from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.spike import views

urlpatterns = [
    path("projects/<uuid:code>/add_spike/", views.add_spike, name="hc-add-spike"),
]
