from pytest_bdd import scenarios, when, then, parsers
from tests.page_objects.demoqa_menu_page import MenuPage
from tests.page_objects.swisnl_jquery_demo_page import ContextMenuPage
from tests.page_objects.demoqa_buttons_page import ButtonPage
from tests.page_objects.sel08_click_and_hold_page import ClickAndHoldPage
from tests.page_objects.theinternet_hovers_page import HoversPage

# Load all the scenarios from the feature file
scenarios("../features/action_chains.feature")

@when('I hover over the "Main Item 2" menu')
def hover_on_menu_item2(driver):
    MenuPage(driver).hover_on_menu_item2()

@then("I should see the submenu")
def verify_visibility_of_sub_menu(driver):
    MenuPage(driver).verify_visibility_of_sub_menu()

@when("I right-click on the context menu button")
def right_click_on_menu(driver):
    ContextMenuPage(driver).right_click_on_menu()

@when(parsers.parse('I select "{option}" from the context menu'))
def click_on_option(driver, option: str):
    ContextMenuPage(driver).click_on_option(option)

@then(parsers.parse('I should see an alert with the message "{message}"'))
def verify_msg_on_alert(driver, message: str):
    ContextMenuPage(driver).verify_msg_on_alert(message)

@when('I double-click on the "Double Click Me" button')
def double_click_on_btn(driver):
    ButtonPage(driver).double_click_on_btn()

@then(parsers.parse('I should see a confirmation message as "{message}"'))
def verify_msg_after_doubleclck(driver, message: str):
    ButtonPage(driver).verify_msg_after_doubleclck(message)

@when(parsers.parse('I hover over the second avatar and click on the "{link_text}" link'))
def hover_and_click_on_second_user(driver, link_text: str):
    HoversPage(driver).hover_and_click_on_second_user(link_text)

@then("I should be navigated to the profile page")
def verify_navigation_to_profile(driver):
    HoversPage(driver).verify_navigation_to_profile()

@when('I move "C" to the position of item "A"')
def hold_item_C(driver):
    ClickAndHoldPage(driver).move_C_to_position_A()

@then('the positions of item "C" and item "A" should be interchanged')
def verify_order_of_A_and_C(driver):
    ClickAndHoldPage(driver).verify_order_of_A_and_C()