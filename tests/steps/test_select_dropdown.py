from pytest_bdd import scenarios, when, then, parsers
from tests.page_objects.mobiscroll_select_page import SelectDropdownPage

# Load all the scenarios from the feature file
scenarios("../features/select_dropdown.feature")

@when(parsers.parse('I select "{option1}" and "{option2}" from the dropdown'))
def select_multiple_options(driver, option1: str, option2: str):
    select_page = SelectDropdownPage(driver)
    select_page.select_options(option1, option2)

@then(parsers.parse('both options "{option1}" and "{option2}" should be selected'))
def verify_selected_options(driver, option1: str, option2: str):
    select_page = SelectDropdownPage(driver)
    assert select_page.get_selected_options() == ["Books", "Health & Beauty"], \
    f"Expected options '{option1}' and '{option2}' to be selected, but got different options."