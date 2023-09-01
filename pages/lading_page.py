from pages.base_page import Page
from selenium.webdriver.common.by import By


class LadingPage(Page):

    DOWNLOAD_BTN = (By.CSS_SELECTOR, 'a[href*="app.curesk.in/KSjEbBWqQN"] span.elementor-button-text')

    def open_page(self):
        self.driver.get('https://cureskin.com/')
    
    def click_download_btn(self):
        self.wait_for_element_to_be_clickable_and_click(*self.DOWNLOAD_BTN)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
