from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ClickAndHoldPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.click_and_hold = None
        self.actions = ActionChains(driver)
        self.letter_A_locator = (By.NAME, "A")
        self.letter_C_locator = (By.NAME, "C")
        self.list_items_locator = (By.CLASS_NAME, "ui-state-default")

    def move_C_to_position_A(self):
        letter_C_element = self.driver.find_element(*self.letter_C_locator)
        letter_A_element = self.driver.find_element(*self.letter_A_locator)
        self.actions.click_and_hold(letter_C_element)\
            .move_to_element(letter_A_element)\
            .move_by_offset(-15, 0)\
            .pause(1)\
            .release()\
            .perform()

    def verify_order_of_A_and_C(self):
        letters = self.driver.find_elements(*self.list_items_locator)

        assert letters[0].text == "C", f"The first letter is not C, instead it is {letters[0].text}"
        assert letters[1].text == "A", f"The second letter is not A, instead it is {letters[1].text}"