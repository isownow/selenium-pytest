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

    def login(self, email: str, password: str):
        # Click on Sign Up/Login tab
        self.driver.find_element(*self.logintab_locator).click()

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

    def validate_invalid_creds_message(self):
        # Validate whether 'Your email or password is incorrect!' text is visible
        displayText = self.driver.find_element(*self.invalid_creds_msg_locator).text
        assert displayText == "Your email or password is incorrect!"

    def validate_popup_message(self, scenario: Literal["empty_email", "empty_password", "email_incomplete", "email_domain_incorrect", "email_without_@"], input: str):
        if "email" in scenario:
            field = self.driver.find_element(*self.email_locator)
        elif "password" in scenario:
            field = self.driver.find_element(*self.password_locator)
        else:
            raise Exception("This scenario has not been configured in the test.")
        
        # Get the validation message using JavaScript
        message = self.driver.execute_script("return arguments[0].validationMessage;", field)

        # Validate the pop up message
        if ("empty" in scenario):
            assert message == "Please fill out this field."
        elif (scenario == "email_incomplete"):
            assert message == f"Please enter a part following '@'. '{input}' is incomplete."
        elif (scenario == "email_without_@"):
            assert message == f"Please include an '@' in the email address. '{input}' is missing an '@'."
        elif (scenario == "email_domain_incorrect"):
            assert message == f"A part following '@' should not contain the symbol '@'."
        else:
            raise Exception("This scenario has not been configured in the test.")

