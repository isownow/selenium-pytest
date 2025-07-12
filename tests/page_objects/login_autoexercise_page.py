import json
import os
import time
from typing import Literal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.COOKIES_FILE = "tests/data/automationexercise_cookies.json"
        self.logintab_locator = (By.CSS_SELECTOR, "a[href='/login']")
        self.email_locator = (By.CSS_SELECTOR, "[data-qa='login-email']")
        self.password_locator = (By.CSS_SELECTOR, "[data-qa='login-password']")
        self.loginbtn_locator = (By.CSS_SELECTOR, "[data-qa='login-button']")
        self.display_text_locator = (By.CSS_SELECTOR, "a:has(i.fa-user)")   
        self.invalid_creds_msg_locator = (By.CSS_SELECTOR, "p[style='color: red;']")

    def get_and_add_cookies(self):
        # # manual login
        # self.go_to_login_page()
        # self.enter_credentials_and_login("johnsmith09@jon.com", "D0cker!Xyz")
        # self.validate_url_post_login()
        # # get cookies
        # with open(self.COOKIES_FILE, "w") as f:
        #     json.dump(self.driver.get_cookies(), f)

        # add cookies
        with open(self.COOKIES_FILE, "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        # refresh
        self.driver.refresh()
        print(self.driver.current_url) # https://automationexercise.com/login
        time.sleep(5)

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

    def do_login(self, email: str, password: str):
        self.go_to_login_page()
        self.enter_credentials_and_login(email, password)
        self.validate_url_post_login()

    def validate_display_text_post_login(self, name: str):
        # Validate whether 'Logged in as user' text is visible
        displayText = self.driver.find_element(*self.display_text_locator).text
        assert displayText == f"Logged in as {name}", "The user is not logged in!"

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
    
    def get_cookies(self):
        with open(self.COOKIES_FILE, "w") as f:
            json.dump(self.driver.get_cookies(), f)

    def add_cookies(self):
        with open(self.COOKIES_FILE, "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
    
    def load_existing_cookies(self, email: str, password: str):
        if os.path.exists(self.COOKIES_FILE):
            self.add_cookies()
            self.driver.refresh()
        else:
            self.do_login(email, password)
            self.get_cookies()

    def check_session_validity(self, email: str, password: str):
        if self.driver.current_url == "https://automationexercise.com/login":
            print("Either the cookies have expired or session is invalid, will login again and get the cookies...")
            self.do_login(email, password)
            self.get_cookies()

    def add_cookies_in_new_session(self, name: str):
        self.driver._already_quit = True
        self.driver.quit()

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://automationexercise.com")
        self.add_cookies()
        self.driver.refresh()

        self.validate_display_text_post_login(name)

        self.driver.quit()