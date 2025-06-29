# tests/steps/common_steps.py
from pytest_bdd import given, parsers

@given(parsers.parse('I open the website "{url}"'))
@given(parsers.parse('the user opens the website "{url}"'))
def open_website(driver, url):
    driver.get(url)