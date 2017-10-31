from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate data for automated testing and manual review"

    def handle(self, **_options):
        pass
