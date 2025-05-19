import json
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.login_page import LoginPage

@pytest.fixture
def login_page(browserInstance: WebDriver):
    return LoginPage(browserInstance)

test_data_path = "tests/data/login_data.json"
with open(test_data_path) as f:
    test_data = json.load(f)

valid_cred_list = test_data["validCreds"]
valid_cred_dict = test_data["validCreds"][0]
incorrect_email_list = test_data["incorrectLoginFields"]["email"]
invalid_email_list = test_data["invalidEmails"]
incorrect_password_list = test_data["incorrectLoginFields"]["password"]

@pytest.mark.positive
@pytest.mark.parametrize("valid_cred", valid_cred_list)
def test_valid_credentials(login_page: LoginPage, valid_cred: dict[str, str]):
    login_page.login(valid_cred["email"], valid_cred["password"])
    login_page.validate_url_post_login()
    login_page.validate_display_text_post_login(valid_cred["name"])

@pytest.mark.negative
@pytest.mark.parametrize("incorrect_email", incorrect_email_list)
def test_incorrect_email(login_page: LoginPage, incorrect_email: str):
    login_page.login(incorrect_email, valid_cred_dict["password"])
    login_page.validate_invalid_creds_message()

@pytest.mark.negative
@pytest.mark.parametrize("incorrect_password", incorrect_password_list)
def test_incorrect_password(login_page: LoginPage, incorrect_password: str):
    login_page.login(valid_cred_dict["email"], incorrect_password)
    login_page.validate_invalid_creds_message()

@pytest.mark.negative
def test_empty_email(login_page: LoginPage):
    login_page.login("", valid_cred_dict["password"])
    login_page.validate_popup_message("empty_email", "")

@pytest.mark.negative
def test_empty_password(login_page: LoginPage):
    login_page.login(valid_cred_dict["email"], "")
    login_page.validate_popup_message("empty_password", "")

@pytest.mark.negative
@pytest.mark.parametrize("invalid_email", invalid_email_list)
def test_invalid_email(login_page: LoginPage, invalid_email: str):
    login_page.login(invalid_email, valid_cred_dict["password"])
    scenario: str
    if invalid_email.endswith("@"):
        scenario = "email_incomplete"
    elif "@" not in invalid_email:
        scenario = "email_without_@"
    elif invalid_email.count("@") > 1:
        scenario = "email_domain_incorrect"
    else:
        raise Exception("This invalid email scenario needs to be configured.")

    login_page.validate_popup_message(scenario, invalid_email)