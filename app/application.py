from pages.lading_page import LadingPage
from pages.header import Header
from pages.about_us_page import AboutUsPage
from pages.testimonials_page import TestimonialsPage
from pages.expertise_page import ExpertisePage
from pages.shop_page import ShopPage
from pages.contact_us_page import ContactUsPage
from pages.footer import Footer
from pages.shop_header import ShopHeader

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.landing_page = LadingPage(self.driver)
        self.header = Header(self.driver)
        self.about_us_page = AboutUsPage(self.driver)
        self.testimonials_page = TestimonialsPage(self.driver)
        self.expertise_page = ExpertisePage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.contact_us_page = ContactUsPage(self.driver)
        self.footer = Footer(self.driver)
        self.shop_header = ShopHeader(self.driver)
