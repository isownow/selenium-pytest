from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ButtonPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.doubleclck_btn_locator = (By.ID, "doubleClickBtn")
        self.doubleclck_msg_locator = (By.ID, "doubleClickMessage")

    def double_click_on_btn(self):
        doubleclck_btn_element = self.driver.find_element(*self.doubleclck_btn_locator)
        self.actions.double_click(doubleclck_btn_element).perform()
        self.actions.click_and_hold(doubleclck_btn_element)

    def verify_msg_after_doubleclck(self, expected_msg: str):
        actual_msg = self.driver.find_element(*self.doubleclck_msg_locator).text
        assert actual_msg == expected_msg, f"Expected '{expected_msg}', but got '{actual_msg}'"

    