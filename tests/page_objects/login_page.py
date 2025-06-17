from typing import Literal
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logintab_locator = (By.CSS_SELECTOR, "a[href='/login']")
        self.email_locator = (By.CSS_SELECTOR, "[data-qa='login-email']")
        self.password_locator = (By.CSS_SELECTOR, "[data-qa='login-password']")
        self.loginbtn_locator = (By.CSS_SELECTOR, "[data-qa='login-button']")
        self.display_text_locator = (By.CSS_SELECTOR, "a:has(i.fa-user)")   
        self.invalid_creds_msg_locator = (By.CSS_SELECTOR, "p[style='color: red;']")

    def go_to_login_page(self):
        # Click on Sign Up/Login tab
        self.driver.find_element(*self.logintab_locator).click()

    def enter_credentials_and_login(self, email: str, password: str):
        # Enter valid credentials
        self.driver.find_element(*self.email_locator).send_keys(email)
        self.driver.find_element(*self.password_locator).send_keys(password)

        # Click login button
        self.driver.find_element(*self.loginbtn_locator).click()

    def validate_url_post_login(self):
        # Confirm whether the user is redirected to the home page URL after logging in
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be("https://automationexercise.com/"))
        except TimeoutException:
            assert False, "Login failed: Home page not loaded after login!"

    def validate_display_text_post_login(self, name: str):
        # Validate whether 'Logged in as user' text is visible
        displayText = self.driver.find_element(*self.display_text_locator).text
        assert displayText == f"Logged in as {name}"

    def get_error_message(self):
        return self.driver.find_element(*self.invalid_creds_msg_locator).text
    
    def get_error_message_invalid_scenario(self):
        return self.driver.find_element(*self.invalid_creds_msg_locator).text

    def get_popup_message(self, scenario: Literal["empty_email", "empty_password", "email_incomplete", "email_domain_incorrect", "email_without_@"], input: str):
        if "email" in scenario:
            field = self.driver.find_element(*self.email_locator)
        elif "password" in scenario:
            field = self.driver.find_element(*self.password_locator)
        else:
            raise Exception("This scenario has not been configured in the test.")
        
        # Get the validation message using JavaScript
        return self.driver.execute_script("return arguments[0].validationMessage;", field)

