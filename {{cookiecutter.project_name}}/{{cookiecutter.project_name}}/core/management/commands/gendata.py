import random
from contextlib import suppress
import logging

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from faker import Faker


logging.getLogger('backend').setLevel(logging.WARNING)


class Command(BaseCommand):
    help = "Generate data for automated testing and manual review"

    fake = Faker()

    def add_arguments(self, parser):
        parser.add_argument(
            'emails',
            nargs='?',
            type=lambda value: value.split(','),
            default=[],
        )

    def handle(self, *, emails, **_options):
        pass
