from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class DynamicControlsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.enable_btn_locator = (By.CSS_SELECTOR, "#input-example > button")
        self.input_locator = (By.CSS_SELECTOR, "input[type='text']")
        self.input_box = self.driver.find_element(*self.input_locator)

    def click_on_enable_btn(self):
        self.driver.find_element(*self.enable_btn_locator).click()

    def wait_till_input_field_enables(self, timeout=5):
        WebDriverWait(self.driver, timeout, poll_frequency=0.2, ignored_exceptions=[NoSuchElementException, ElementNotInteractableException]).until(lambda d: self.input_box.is_enabled())

    def type_text_in_input_field(self, text: str):
        self.input_box.send_keys(text)

        actual_text = self.input_box.get_attribute("value")

        assert actual_text == text, f"The text in the input box is not {text}, instead it is {actual_text}"