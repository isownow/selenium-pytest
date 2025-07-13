from pytest_bdd import scenarios, when, then, parsers
from tests.page_objects.theinternet_dynamic_controls_page import DynamicControlsPage

# Load all the scenarios from the feature file
scenarios("../features/fluent_wait.feature")

@when(parsers.parse('I click on the Enable button'))
def click_on_enable_btn(driver):
    DynamicControlsPage(driver).click_on_enable_btn()

@then("I wait for the input field to be enabled using Fluent Wait")
def wait_till_input_field_enables(driver):
    DynamicControlsPage(driver).wait_till_input_field_enables()

@then(parsers.parse('I type "{text}" into the input field'))
def type_text_in_input_field(driver, text: str):
    DynamicControlsPage(driver).type_text_in_input_field(text)