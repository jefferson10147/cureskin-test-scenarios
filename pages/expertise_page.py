from pages.base_page import Page


class ExpertisePage(Page):
    
    def verify_page_is_opened(self):
        expected_url = 'https://cureskin.com/expertise/'
        self.verify_partial_url(expected_url)
