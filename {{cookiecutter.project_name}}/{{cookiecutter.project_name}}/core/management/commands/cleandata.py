from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Clean up existing data"

    def handle(self, **_options):
        pass
