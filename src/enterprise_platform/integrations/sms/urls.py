from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.sms import views

urlpatterns = [
    path("projects/<uuid:code>/add_sms/", views.add, name="hc-add-sms"),
]
