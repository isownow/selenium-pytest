from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StepperFormPage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.name_locator = (By.CSS_SELECTOR, "input[placeholder='Enter your name']")
        self.email_locator = (By.CSS_SELECTOR, "input[placeholder='Enter your email']")
        self.nextbtn_locator = (By.CSS_SELECTOR, ".step-content.active .btn-next")
        self.submitbtn_locator = (By.CSS_SELECTOR, ".btn-submit")

    def fill_form(self):
        self.driver.find_element(*self.name_locator).send_keys("John Smith")
        self.driver.find_element(*self.nextbtn_locator).click()
        self.driver.find_element(*self.email_locator).send_keys("johns1290@example.com")
        self.driver.find_element(*self.nextbtn_locator).click()

    def click_submit(self):
        self.driver.find_element(*self.submitbtn_locator).click()

    def wait_for_alert_and_verify(self, expected_msg: str, timeout=10):
        # Alerts don’t always appear immediately after the form is submitted. Without the wait, Selenium might check for the alert before it exists, throwing a NoAlertPresentException. This line ensures your test pauses just long enough to let the alert appear.
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        actual_msg = self.driver.switch_to.alert.text
        assert actual_msg == expected_msg, f"Expected '{expected_msg}', but got '{actual_msg}'"
        self.driver.switch_to.alert.accept()