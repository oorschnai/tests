from __future__ import annotations

import json
from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from enterprise_platform.accounts.http import AuthenticatedHttpRequest
from enterprise_platform.api.models import Channel
from enterprise_platform.front.decorators import require_setting
from enterprise_platform.front.views import _get_rw_project_for_user
from enterprise_platform.integrations.opsgenie import forms


@require_setting("OPSGENIE_ENABLED")
@login_required
def add(request: AuthenticatedHttpRequest, code: UUID) -> HttpResponse:
    project = _get_rw_project_for_user(request, code)

    if request.method == "POST":
        form = forms.AddOpsgenieForm(request.POST)
        if form.is_valid():
            channel = Channel(project=project, kind="opsgenie")
            v = {"region": form.cleaned_data["region"], "key": form.cleaned_data["key"]}
            channel.value = json.dumps(v)
            channel.save()

            channel.assign_all_checks()
            return redirect("hc-channels", project.code)
    else:
        form = forms.AddOpsgenieForm()

    ctx = {"page": "channels", "project": project, "form": form}
    return render(request, "add_opsgenie.html", ctx)
