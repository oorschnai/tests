from __future__ import annotations

from unittest.mock import Mock, patch

from enterprise_platform.api.management.commands.prunepingsslow import Command
from enterprise_platform.api.models import Check, Ping
from enterprise_platform.test import BaseTestCase


class PrunePingsSlowTestCase(BaseTestCase):
    @patch("enterprise_platform.api.models.remove_objects", autospec=True)
    def test_it_works(self, remove_objects: Mock) -> None:
        check = Check.objects.create(project=self.project, n_pings=101)
        Ping.objects.create(owner=check, n=1)
        Command(stdout=Mock()).handle()

        # The ping should have been deleted
        self.assertFalse(Ping.objects.exists())
