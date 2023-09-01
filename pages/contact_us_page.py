from pages.base_page import Page
from selenium.webdriver.common.by import By


class ContactUsPage(Page):

    PAGE_TITLE = (By.CSS_SELECTOR, 'h1.elementor-heading-title.elementor-size-default')

    def verify_page_is_opened(self):
        expected_url = 'https://cureskin.com/contact/'
        self.verify_partial_url(expected_url)

    def verify_page_title(self):
        expected_title = 'Connect With Us'
        actual_text = self.find_element(*self.PAGE_TITLE).text
        actual_text = actual_text.strip().replace('\n', ' ')
        assert actual_text == expected_title, f'Error, expected {expected_title} did not match actual {actual_text}'
