# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from faker import Faker
from expecter import expect

from . import user


fake = Faker()


def describe_signup():

    def with_duplicate_username():
        user.signup('Admin', fake.email(), 'password')
        expect(user.browser) \
            .has_text("A user with that username already exists.")


def describe_login():

    def with_valid_credentials():
        user.login('admin', 'password')
        expect(user.browser.url) == user.site + "/feed"

        user.logout()
        expect(user.browser.url) == user.site + "/login"

    def with_invalid_username():
        user.login('bad_username', 'password')
        expect(user.browser).has_text(
            "Unable to log in with provided credentials.")
        expect(user.browser.url) == user.site + "/login"

    def with_invalid_password():
        user.login('admin', 'bad_password')
        expect(user.browser).has_text(
            "Unable to log in with provided credentials.")
        expect(user.browser.url) == user.site + "/login"

    def with_alternate_case_username():
        user.login('Admin', 'password')
        expect(user.browser.url) == user.site + "/feed"


def describe_navbar():

    def describe_home():

        def when_public():
            user.logout()
            user.goto_home(_login=False)
            expect(user.browser.url) == user.site + "/"
            expect(user.browser).has_text("Your playlist for everything.")
            expect(user.browser).has_text("Get started")

        def when_auth():
            user.goto_home()
            expect(user.browser.url) == user.site + "/feed"

    def describe_queue():

        def when_auth():
            user.goto_queue()
            expect(user.browser.url) == user.site + "/queue"
            expect(user.browser).has_text("Queue")

    def describe_feed():

        def when_auth():
            user.goto_feed()
            expect(user.browser.url) == user.site + "/feed"
            expect(user.browser).has_text("Inbox")
            expect(user.browser).has_text("Activity")

    def describe_search():

        def when_auth():
            user.goto_search()
            expect(user.browser.url) == user.site + "/search"


def describe_search():

    def with_results():
        user.search("road")
        expect(user.browser).has_text("Abbey Road")

    def with_no_results():
        user.search("foobar")
        expect(user.browser).has_text("No Results Found")

    def it_can_search_using_enter_key():
        user.search("make", use_enter=True)
        expect(user.browser).has_text("Make Happy")


def describe_errors():

    def when_404():
        user.login()
        user.visit("/foobar")
        expect(user.browser) \
            .has_text("Sorry we couldn't find what you're looking for.")
