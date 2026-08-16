from __future__ import annotations

from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from enterprise_platform.accounts.http import AuthenticatedHttpRequest
from enterprise_platform.api.models import Channel
from enterprise_platform.front.decorators import require_setting
from enterprise_platform.front.views import _get_rw_project_for_user
from enterprise_platform.integrations.zulip import forms


@require_setting("ZULIP_ENABLED")
@login_required
def add(request: AuthenticatedHttpRequest, code: UUID) -> HttpResponse:
    project = _get_rw_project_for_user(request, code)

    if request.method == "POST":
        form = forms.AddZulipForm(request.POST)
        if form.is_valid():
            channel = Channel(project=project, kind="zulip")
            channel.value = form.get_value()
            channel.save()

            channel.assign_all_checks()
            return redirect("hc-channels", project.code)
    else:
        form = forms.AddZulipForm()

    ctx = {"page": "channels", "project": project, "form": form}
    return render(request, "add_zulip.html", ctx)
