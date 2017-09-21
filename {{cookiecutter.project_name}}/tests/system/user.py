site = None
browser = None


def visit(path):
    browser.visit(site + path)


def goto_index():
    browser.find_by_css('.navbar-brand').first.click()


def search(query):
    browser.find_by_id('id_text').fill(query)
    browser.find_by_id('id_search').first.click()


def clear_search():
    browser.find_by_css('.btn-danger').first.click()
