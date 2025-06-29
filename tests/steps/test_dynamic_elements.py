from pytest_bdd import scenarios, when, then, parsers
from tests.page_objects.tac_stepper_form_page import StepperFormPage
from tests.page_objects.theinternet_dynamic_loading1_page import DynamicLoading1Page
from tests.page_objects.demoqa_dynamicprop_page import DynamicPropertiesPage

# Load all scenarios from the feature file  
scenarios("../features/dynamic_elements.feature") 

@when("I fill in the form with valid data")
def fill_form(driver):
    StepperFormPage(driver).fill_form()

@when("I click the Submit button")
def click_submit(driver):
    StepperFormPage(driver).click_submit()

@then(parsers.parse('I should see a dynamic alert with the message "{message}"'))
def verify_alert(driver, message: str):
    StepperFormPage(driver).wait_for_alert_and_verify(message)

@when("I click the Start button")
def click_start(driver):
    DynamicLoading1Page(driver).click_start()

@then(parsers.parse('I should wait until the "{text}" text is visible'))
def verify_text(driver, text: str):
    DynamicLoading1Page(driver).wait_for_text_and_verify(text)

@when("I wait for the first button to become enabled")
def wait_dynamic_button(driver):
    DynamicPropertiesPage(driver).wait_for_button_enablement()

@then("I should be able to click the button without error")
def successful_click(driver):
    DynamicPropertiesPage(driver).click_first_btn()

@when('I wait for the button to change its text color')
def wait_for_text_color_change(driver):
    DynamicPropertiesPage(driver).wait_for_text_color_change()

@then(parsers.parse('the button\'s text color is changed to red "{expected_color}"'))
def verify_text_color_change(driver, expected_color):
    DynamicPropertiesPage(driver).verify_text_color_change(expected_color)
# @when("I click the Remove button")
# def remove_checkbox(driver):
#     herokuapp_page.DynamicControls(driver).remove_checkbox()

# @then("I should wait until the checkbox disappears")
# def checkbox_should_disappear(driver):
#     herokuapp_page.DynamicControls(driver).wait_until_checkbox_disappears()

# @then("I should not get a stale element exception")
# def no_stale_element_issue(driver):
#     pass  # If it passed to here, no stale exception happened

# @when("I fetch the number of rows and columns")
# def fetch_table(driver):
#     guru99_table_page.DynamicTable(driver).print_table_summary()

# @then("I should print the company names and current prices")
# def print_table_content(driver):
#     pass  # Already printed

# @when("I click the Show Small Modal button")
# def open_modal(driver):
#     demoqa_page.ModalPopup(driver).open_small_modal()

# @then("I should wait for the modal to appear")
# def modal_appears(driver):
#     demoqa_page.ModalPopup(driver).wait_for_modal()

# @then("I should close the modal successfully")
# def close_modal(driver):
#     demoqa_page.ModalPopup(driver).close_modal()

# @when("I switch to the first iframe")
# def switch_to_iframe(driver):
#     demoqa_page.IframeContent(driver).switch_to_frame()

# @then("I should verify the heading inside the iframe")
# def iframe_content(driver):
#     assert "This is a sample page" in driver.page_source