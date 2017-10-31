import expecter


def has_text(browser, text):
    return browser.is_text_present(text)


expecter.add_expectation(has_text)
