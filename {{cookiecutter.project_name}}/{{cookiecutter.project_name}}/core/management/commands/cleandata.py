import logging

from django.core.management.base import BaseCommand

from backend.media.models import Recommendation, Link


log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Clean up existing data"

    def handle(self, **_options):
        pass
