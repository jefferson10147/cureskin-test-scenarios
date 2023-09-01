from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):

    LOGO = (By.CSS_SELECTOR, 'img[src*="logo.png"]')
    MENU = (By.CSS_SELECTOR, 'ul#menu-1-5bfd1d9 li')

    def verify_presence_of_logo(self):
        self.wait_for_element_clickable(*self.LOGO)

    def verify_presence_of_menu_elements(self):
        total_of_menu_elements = 9
        menu_elements = self.find_elements(*self.MENU)
        assert len(menu_elements) == total_of_menu_elements, \
            f'Expected 6 menu elements, but got {len(menu_elements)}'

    def verify_redirection_to_right_page(self):
        expected_url = 'https://play.google.com/'
        self.verify_partial_url(expected_url)
