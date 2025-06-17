import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pytest_bdd import scenario

from tests.steps.login_steps import *
from tests.page_objects.login_page import LoginPage

@pytest.fixture
def login_page(browserInstance: WebDriver):
    return LoginPage(browserInstance)

@allure.feature("Login Feature")
@allure.story("Successful login")
@pytest.mark.positive
@scenario("login.feature", "Successful login")
def test_login_success():
    pass

@allure.feature("Login Feature")
@allure.story("Login with incorrect email")
@pytest.mark.negative
@scenario("login.feature", "Login with incorrect email")
def test_login_incorrect_email():
    pass

@allure.feature("Login Feature")
@allure.story("Login with incorrect password")
@pytest.mark.negative
@scenario("login.feature", "Login with incorrect password")
def test_login_incorrect_password():
    pass

@allure.feature("Login Feature")
@allure.story("Login with invalid email/password")
@pytest.mark.negative
@scenario("login.feature", "Login with invalid email/password")
def test_login_invalid_email_password():
    pass

    
