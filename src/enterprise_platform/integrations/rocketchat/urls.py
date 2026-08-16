from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.rocketchat import views

urlpatterns = [
    path("integrations/rocketchat/", views.rocketchat_help, name="hc-rocketchat-help"),
    path("projects/<uuid:code>/add_rocketchat/", views.add, name="hc-add-rocketchat"),
]
