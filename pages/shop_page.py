from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage(Page):

    PAGE_URL = 'https://shop.cureskin.com/collections/all'
    LAYAOUT_THREE_BTN = (By.XPATH, '//button[@data-layout-mode="grid-3"]')
    SORT_BY = (By.CSS_SELECTOR, '.disclosure-has-popup.facets__disclosure.facet-filters__sort')
    SORT_BY_SELLING = (By.XPATH, '//label[@for="Filter-best-selling-2"]')
    SORT_BY_ALPHABETICALLY = (By.XPATH, '//label[@for="Filter-title-ascending-3"]')
    SORT_BY_ALPHABETICALLY_DESC = (By.XPATH, '//label[@for="Filter-title-descending-4"]')
    SORT_BY_DATE_OLD_TO_NEW = (By.XPATH, '//label[@for="Filter-created-ascending-7"]')
    SORT_BY_DATE_NEW_TO_OLD = (By.XPATH, '//label[@for="Filter-created-descending-8"]')

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

    def click_sort_by_alphabetically_descending(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SORT_BY_ALPHABETICALLY_DESC)

    def click_sort_by_date_old_to_new_option(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SORT_BY_DATE_OLD_TO_NEW)

    def click_sort_by_date_new_to_old_option(self):
        self.wait_for_element_to_be_clickable_and_click(*self.SORT_BY_DATE_NEW_TO_OLD)

    def verify_url_contains_sort_query(self, query):
        self.verify_partial_url(query)
