from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DynamicLoading1Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.startbtn_locator = (By.CSS_SELECTOR, "#start button")
        self.text_locator = (By.CSS_SELECTOR, "#finish h4")

    def click_start(self):
        self.driver.find_element(*self.startbtn_locator).click()

    def wait_for_text_and_verify(self, expected_text: str, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.text_locator))
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
