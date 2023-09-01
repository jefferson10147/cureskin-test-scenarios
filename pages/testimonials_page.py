from pages.base_page import Page


class TestimonialsPage(Page):

    def verify_page_is_opened(self):
        expected_url = 'https://cureskin.com/testimonials/'
        self.verify_partial_url(expected_url)
