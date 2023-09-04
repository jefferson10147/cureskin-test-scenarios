from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage(Page):

    PAGE_URL = 'https://shop.cureskin.com/collections/all'
    LAYAOUT_THREE_BTN = (By.XPATH, '//button[@data-layout-mode="grid-3"]')
    SORT_BY = (By.CSS_SELECTOR, '.disclosure-has-popup.facets__disclosure.facet-filters__sort')
    SORT_BY_SELLING = (By.XPATH, '//label[@for="Filter-best-selling-2"]')
    SORT_BY_ALPHABETICALLY = (By.XPATH, '//label[@for="Filter-title-ascending-3"]')

    def open_page(self):
        self.open_url(self.PAGE_URL)

    def verify_page_is_opened(self):
        expected_url = self.PAGE_URL
        self.verify_partial_url(expected_url)

    def click_layout_three_btn(self):
        self.wait_for_element_to_be_clickable_and_click(*self.LAYAOUT_THREE_BTN)

    def click_sort_by_option(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SORT_BY)

    def click_sort_by_selling(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SORT_BY_SELLING)

    def click_sort_by_alphabetically(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SORT_BY_ALPHABETICALLY)

    def verify_url_contains_sort_query(self, query):
        self.verify_partial_url(query)
