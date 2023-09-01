from pages.base_page import Page


class ShopPage(Page):

    def verify_page_is_opened(self):
        expected_url = 'https://shop.cureskin.com/collections/all'
        self.verify_partial_url(expected_url)
