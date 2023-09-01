from pages.lading_page import LadingPage
from pages.header import Header
from pages.about_us_page import AboutUsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.landing_page = LadingPage(self.driver)
        self.header = Header(self.driver)
        self.about_us_page = AboutUsPage(self.driver)
