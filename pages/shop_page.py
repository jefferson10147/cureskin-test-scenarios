from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShopPage(Page):

    PAGE_URL = 'https://shop.cureskin.com/collections/all'
    LAYAOUT_THREE_BTN = (By.XPATH, '//button[@data-layout-mode="grid-3"]')

    def open_page(self):
        self.open_url(self.PAGE_URL)

    def verify_page_is_opened(self):
        expected_url = self.PAGE_URL
        self.verify_partial_url(expected_url)

    def click_layout_three_btn(self):
        self.wait_for_element_to_be_clickable_and_click(*self.LAYAOUT_THREE_BTN)
