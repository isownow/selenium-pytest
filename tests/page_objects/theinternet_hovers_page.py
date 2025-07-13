from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class HoversPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.action_chains = ActionChains(driver)
        self.cards_locator = (By.CLASS_NAME, "figure")
        self.card_locator = (By.TAG_NAME, "h5")
        self.second_user_text = "name: user2"
        self.second_user_profile_url = "/users/2"

    def hover_and_click_on_second_user(self, link_text):
        # Since we are going to iterate over a list of WebElements, we are using find_elements
        cards = self.driver.find_elements(*self.cards_locator)
        self.user_profile_link_locator = (By.LINK_TEXT, link_text)

        for card in cards:
            try:
                # hover over the user
                self.action_chains.move_to_element(card).perform()
                # get the user name text
                user_text = card.find_element(*self.card_locator).text.strip()
                # check if that is the user we want, if not then continue iterating
                if user_text == self.second_user_text:
                    # we found the user, click on the profile link
                    card.find_element(*self.user_profile_link_locator).click()
                    break
            except NoSuchElementException:
                continue

    def verify_navigation_to_profile(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(self.second_user_profile_url))
        except TimeoutException:
            raise AssertionError(f"Timed out waiting for URL to contain: {self.second_user_profile_url}. Actual URL: {self.driver.current_url}")