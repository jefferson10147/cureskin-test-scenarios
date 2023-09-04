from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShopHeader(Page):

    CART_ICON = (By.ID, 'cart-icon-bubble')

    def click_cart_icon(self):
        self.wait_for_element_to_be_clickable_and_click(*self.CART_ICON)
