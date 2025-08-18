from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SelectDropdownPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.multi_select_locator = (By.ID, "multiple-select-select")

    def select_options(self, *options: str):
        dropdown = self.driver.find_element(*self.multi_select_locator)

        # The dropdown is hidden (display: none), so Selenium can locate it but can’t interact with it directly.
        # If the dropdown is meant to be interacted with but just hidden by default, you can force it to display
        self.driver.execute_script("arguments[0].style.display = 'block';", dropdown)

        select = Select(dropdown)
        for option in options:
            select.select_by_visible_text(option)

    def get_selected_options(self):
        dropdown = self.driver.find_element(*self.multi_select_locator)
        options = dropdown.find_elements(By.TAG_NAME, "option")
        return [opt.text for opt in options if opt.is_selected()]