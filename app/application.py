from pages.lading_page import LadingPage
from pages.header import Header


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.landing_page = LadingPage(self.driver)
        self.header = Header(self.driver)
