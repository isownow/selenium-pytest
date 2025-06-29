from pytest_bdd import scenarios, when, then, parsers
from tests.page_objects.seldev_dynamic_page import BoxPage

# Load all the scenarios from the feature file
scenarios("../features/core_concepts.feature")

@when(parsers.parse('I click the "Add a box!" button {n:d} times'))
def click_addbox_btn(driver, n):
    BoxPage(driver).click_addbox_btn(n)

@then(parsers.parse('I wait for {n:d} boxes to appear on the page'))
def wait_for_boxes(driver, n):
    BoxPage(driver).wait_for_boxes(n)