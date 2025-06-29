from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ContextMenuPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.menu_btn_locator = (By.CLASS_NAME, "context-menu-one")

    def get_menu_option_locator(self, option: str):
        return (By.CLASS_NAME, f"context-menu-icon-{option}")

    def right_click_on_menu(self):
        menu_btn_element = self.driver.find_element(*self.menu_btn_locator)
        self.actions.context_click(menu_btn_element).perform()

    def click_on_option(self, option: str):
        submenu_btn_locator = self.get_menu_option_locator(option)
        self.driver.find_element(*submenu_btn_locator).click()

    def verify_msg_on_alert(self, expected_msg: str, timeout: int = 5):
        WebDriverWait(self.driver, timeout=timeout).until(EC.alert_is_present())
        actual_msg = self.driver.switch_to.alert.text

        assert actual_msg == expected_msg, f"Expected '{expected_msg}', but got '{actual_msg}'"
        self.driver.switch_to.alert.accept()
        