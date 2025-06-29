from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BoxPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.addbox_btn_locator = (By.CSS_SELECTOR, "#adder")
        self.boxes_locator = (By.CSS_SELECTOR, ".redbox")

    def click_addbox_btn(self, num_of_times: int):
        for _ in range(num_of_times):
            self.driver.find_element(*self.addbox_btn_locator).click()

    def wait_for_boxes(self, expected_boxes, timeout=5):
        def box_count():
            return len(self.driver.find_elements(*self.boxes_locator))

        try:
            WebDriverWait(self.driver, timeout).until(lambda d: box_count() == expected_boxes)
        except TimeoutException as e:
            actual = box_count()
            raise TimeoutException(f"Waited {timeout}s, found {actual} boxes instead of expected {expected_boxes}.")