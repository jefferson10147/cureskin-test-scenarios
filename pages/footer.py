from pages.base_page import Page
from selenium.webdriver.common.by import By

class Footer(Page):

    FOOTER_LINK = (
        By.CSS_SELECTOR, 
        'div.elementor-container.elementor-column-gap-default div.elementor-widget-container p a'
    )

    def verify_each_link_is_clickable(self):
        footer_links = self.find_elements(*self.FOOTER_LINK)

        for link in footer_links:
            # self.actions.move_to_element(link).perform()
            assert link.is_enabled(), f'Error, {link} is not clickable'
