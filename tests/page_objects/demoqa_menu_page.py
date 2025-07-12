from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from tests.test_utilities.helpers import scroll_into_view

class MenuPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.menu_item2_xpath_locator = (By.XPATH, "//a[text()='Main Item 2']")
        self.menu_item2_css_locator = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > a")
        self.submenu_locator = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul")

    def hover_on_menu_item2(self):
        menu_item_element = self.driver.find_element(*self.menu_item2_xpath_locator)
        scroll_into_view(self.driver, menu_item_element)
        self.actions.move_to_element(menu_item_element).perform()

    def verify_visibility_of_sub_menu(self, timeout=10):
        submenu = self.driver.find_element(*self.submenu_locator)
        scroll_into_view(self.driver, submenu)

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.submenu_locator))

        assert submenu.is_displayed(), "Submenu is not visible after hover"
        