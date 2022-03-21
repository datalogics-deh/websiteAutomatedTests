import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from pywinauto import Application


class ProductFormsFlattenerPage:
    URL = 'https://www.datalogics.com/products/pdf-tools/pdf-forms-flattener/'
    SEARCH_TITLE_TEXT = (By.XPATH, "//*[@data-id = 'f6973eb']//div[1]//h1[1]")
    SEARCH_TRY_FREE_TEXT = (By.XPATH, "//*[@data-id = 'f10683b']//div[1]//h3[1]")
    SELECT_FILE_BUTTON = (By.ID, "dl_flattenforms_uploaded_file")
    TERMS_AND_CONDITIONS_CHECKBOX = (By.ID, "dl_flattenforms_disclaimer_check")
    SUBMIT_BUTTON = (By.ID, "dl_flattenforms_submit_btn")
    DOWNLOAD_REPORT_LINK = (By.ID, "dl_flattenform_download_link")
    PROCESSING_MESSAGE = (By.ID, "dl_flattenforms_processing_msg")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_title_phrase(self):
        return self.browser.find_element(*self.SEARCH_TITLE_TEXT)

    def search_try_free_phrase(self):
        return self.browser.find_element(*self.SEARCH_TRY_FREE_TEXT)

    def select_file(self, file):
        self.browser.find_element(*self.SELECT_FILE_BUTTON).send_keys(file)

    def click_terms_and_conditions_checkbox(self):
        self.browser.find_element(*self.TERMS_AND_CONDITIONS_CHECKBOX).click()

    def click_submit_button(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def wait_on_processing_message_to_be_present(self, wait_time):
        ui.WebDriverWait(self.browser, wait_time).until(expected_conditions.presence_of_element_located(self.PROCESSING_MESSAGE))

    def wait_on_processing_message_to_disappear(self, wait_time):
        ui.WebDriverWait(self.browser, wait_time).until(expected_conditions.invisibility_of_element_located(self.PROCESSING_MESSAGE))

    def verify_download_report(self):
        if len(self.browser.find_elements(*self.DOWNLOAD_REPORT_LINK)) > 0:
            return True
        else:
            return False