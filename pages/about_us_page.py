from pages.base_page import Page


class AboutUsPage(Page):

    def verify_page_is_opened(self):
        expected_url = 'https://cureskin.com/about-cureskin/'
        self.verify_partial_url(expected_url)
