import json
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.remote.webdriver import WebDriver

from tests.page_objects.login_autoexercise_page import LoginPage

test_data_path = "tests/data/login_data.json"
with open(test_data_path) as f:
    test_data = json.load(f)

valid_cred_dict = test_data["validCreds"][0]

# Load all scenarios from the feature file  
scenarios("../features/login.feature")  

@pytest.fixture
def login_page(driver: WebDriver):
    return LoginPage(driver)

@given("the user goes to the login page")
def user_on_login_page(login_page: LoginPage):
    login_page.go_to_login_page()

@when("the user clicks login button by entering the valid credentials")
def user_enters_valid_credentials(login_page: LoginPage):
    login_page.enter_credentials_and_login(valid_cred_dict["email"], valid_cred_dict["password"])

@then("they should be redirected to the home page")
def validate_redirection(login_page: LoginPage):
    login_page.validate_url_post_login()

@then("the user's name should be visible on the homepage")
def validate_username_on_homepage(login_page: LoginPage):
    login_page.validate_display_text_post_login(valid_cred_dict["name"])

@when(parsers.parse("the user clicks login button after entering the valid password but incorrect email {email}"))
def user_enters_valid_credentials(login_page: LoginPage, email: str):
    login_page.enter_credentials_and_login(email, valid_cred_dict["password"])

@when(parsers.parse("the user clicks login button after entering the valid email but incorrect password {password}"))
def user_enters_valid_credentials(login_page: LoginPage, password: str):
    login_page.enter_credentials_and_login(valid_cred_dict["email"], password)

@when(parsers.parse("the user clicks login button after entering the email {email} and password {password}"))
def user_enters_valid_credentials(login_page: LoginPage, email: str, password: str):
    valid_values = {
        "correct_email": valid_cred_dict["email"],
        "correct_password": valid_cred_dict["password"],
        "EMPTY": ""
    }

    email = valid_values.get(email, email)
    password = valid_values.get(password, password)
    login_page.enter_credentials_and_login(email, password)

@then(parsers.parse('an error message "{expected_message}" should be displayed'))
def verify_error_message(login_page: LoginPage, expected_message: str):
    actual_message = login_page.get_error_message()
    assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"

@then(parsers.parse("an error message {expected_message} should be displayed for the {scenario} case with email {email} and password {password}"))
def verify_error_message(login_page: LoginPage, expected_message: str, scenario: str, email: str):
    input = email
    if scenario == "empty_password":
        input = ""
    
    actual_message = login_page.get_popup_message(scenario, input)
    assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"

@when("the cookies are not available, I log in to get the cookies else I add the cookies")
def load_existing_cookies(login_page: LoginPage):
    login_page.load_existing_cookies(valid_cred_dict["email"], valid_cred_dict["password"])

@when("if the session is invalid, I login to get the cookies")
def check_session_validity(login_page: LoginPage):
    login_page.check_session_validity(valid_cred_dict["email"], valid_cred_dict["password"])

@then("I restart the browser session, add cookies and verify successful login")
def add_cookies_in_new_session(login_page: LoginPage):
    login_page.add_cookies_in_new_session(valid_cred_dict["name"])