import time


site = None
browser = None


def visit(path):
    browser.visit(site + path)


def is_loading():
    return browser.is_element_present_by_css('.loading')


def is_logged_in():
    return browser.is_element_present_by_css('.navbar-queue')


def is_logged_out():
    return browser.is_element_present_by_text("login")


def signup(username, email, password):
    logout()

    browser.find_by_text("Sign up").first.click()

    browser.fill('username', username)
    browser.fill('email', email)
    browser.fill('password', password)

    browser.find_by_text("Sign up").first.click()
    wait()


def login(username=None, password=None):
    using_default_credentials = username is None and password is None

    visit("/")
    if using_default_credentials and is_logged_in():
        return

    if using_default_credentials:
        username = "admin"
        password = "password"
    else:
        logout()

    browser.find_by_text("login").first.click()
    assert browser.is_text_present("Access {{cookiecutter.project_name}}")

    browser.fill('username', username)
    browser.fill('password', password)

    browser.find_by_name('login').first.click()
    wait()

    if using_default_credentials:
        assert is_logged_in()


def logout():
    visit("/")
    if is_logged_out():
        return

    browser.find_link_by_partial_text("logout").first.click()
    assert is_logged_out()


def goto_home(_login=True):
    if _login:
        login()

    visit("/")


def wait(delay=0.25):
    time.sleep(delay)
    while is_loading():
        time.sleep(delay)
