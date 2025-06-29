from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests.test_utilities.helpers import scroll_into_view

class DynamicPropertiesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.enableAftr_btn_locator = (By.CSS_SELECTOR, "#enableAfter")
        self.colorChange_btn_locator = (By.CSS_SELECTOR, "button[type='button']#colorChange")
        self.btn_with_red_text = (By.CSS_SELECTOR, "button[type='button'].text-danger")

    def wait_for_button_enablement(self, timeout=10):
        button = self.driver.find_element(*self.enableAftr_btn_locator)
        scroll_into_view(self.driver, button)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

        # If we don't wait here for the button to be clickable, the error received would be - selenium.common.exceptions.ElementClickInterceptedException
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.enableAftr_btn_locator))

    def click_first_btn(self):
        self.driver.find_element(*self.enableAftr_btn_locator).click()

    def wait_for_text_color_change(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.btn_with_red_text))

    def verify_text_color_change(self, expected_color):
        button_element = self.driver.find_element(*self.colorChange_btn_locator)
        new_color = button_element.value_of_css_property("color")
        assert new_color == expected_color, f"Unexpected text color: {new_color}"