# TODO: Upgrade mypy to 0.991+ when django-stubs supports it
# mypy: ignore_errors

import random
from contextlib import suppress

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

import log
from faker import Faker


# from {{cookiecutter.project_name}}.{{cookiecutter.first_app_name}} import models


class Command(BaseCommand):
    help = "Generate data for automated testing and manual review"

    fake = Faker()
    new_user_id = None

    def add_arguments(self, parser):
        parser.add_argument(
            'emails',
            nargs='?',
            type=lambda value: value.split(','),
            default=[],
        )

    def handle(self, *, emails, **_options):
        self.update_site()
        admin = self.get_or_create_superuser()
        self.new_user_id = self.get_or_create_user("newbie@example.com").id
        users = [self.get_or_create_user(email) for email in emails]
        self.generate_review_data(admin, *users)

    def update_site(self):
        site = Site.objects.get(id=1)
        site.name = f"{{cookiecutter.project_name}} {settings.BASE_NAME}"
        site.domain = settings.BASE_DOMAIN
        site.save()
        self.stdout.write(f"Updated site: {site}")

    def get_or_create_superuser(self, username="admin", password="password"):
        try:
            user = User.objects.create_superuser(  # type: ignore
                username=username,
                email=f"{username}@{settings.BASE_DOMAIN}",
                password=password,
            )
            self.stdout.write(f"Created superuser: {user}")
        except IntegrityError:
            user = User.objects.get(username=username)
            self.stdout.write(f"Found superuser: {user}")

        return user

    def get_or_create_user(self, base_email, password="password"):
        username, email_domain = base_email.split('@')

        user, created = User.objects.get_or_create(username=username)
        if email_domain == "example.com":
            user.email = base_email
        else:
            user.email = f"{username}+{settings.BASE_NAME}@{email_domain}"
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(f"Created user: {user}")
        else:
            self.stdout.write(f"Updated user: {user}")

        return user

    def generate_review_data(self, *users):
        count = User.objects.count()
        while count < 50:
            with suppress(IntegrityError):
                user = User.objects.create(
                    username=self.fake_username(),
                )
                self.stdout.write(f"Created user: {user}")
                count += 1

        # TODO: Create additional models here
        log.debug(users)

    def random_user(self, skip=None):
        skip_ids = [self.new_user_id]
        if skip:
            skip_ids.append(skip.id)
        users = User.objects.exclude(id__in=skip_ids)
        return random.choice(users)  # type: ignore

    def fake_username(self):
        return self.fake.name().replace(' ', '').lower()
