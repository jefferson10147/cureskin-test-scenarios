from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):

    LOGO = (By.CSS_SELECTOR, 'img[src*="logo.png"]')
    MENU = (By.CSS_SELECTOR, 'ul#menu-1-5bfd1d9 li')
    ABOUT_US_LINK = (By.CSS_SELECTOR, 'a[href*="/about-cureskin/"]')
    TESTIMONIALS_LINK = (By.CSS_SELECTOR, 'a[href*="/testimonials/"]')
    EXPERTISE_LINK = (By.CSS_SELECTOR, 'a[href*="/expertise/"]')
    SHOP_LINK = (By.CSS_SELECTOR, 'a[href*="/collections/all"]')

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

    def click_about_us(self):
        self.wait_for_element_to_be_clickable_and_click(*self.ABOUT_US_LINK)

    def click_testimonials(self):
        self.wait_for_element_to_be_clickable_and_click(*self.TESTIMONIALS_LINK)

    def click_expertise(self):
        self.wait_for_element_to_be_clickable_and_click(*self.EXPERTISE_LINK)

    def click_shop(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SHOP_LINK)