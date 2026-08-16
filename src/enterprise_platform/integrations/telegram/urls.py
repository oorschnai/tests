from __future__ import annotations

from django.urls import path

from enterprise_platform.integrations.telegram import views

urlpatterns = [
    path("integrations/telegram/", views.telegram_help, name="hc-telegram-help"),
    path("integrations/telegram/bot/", views.telegram_bot, name="hc-telegram-webhook"),
    path("integrations/add_telegram/", views.add, name="hc-add-telegram"),
]
