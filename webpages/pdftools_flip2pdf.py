from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions


class ProductFlip2PdfPage:
    URL = 'https://www.datalogics.com/products/pdf-tools/flip2pdf/'
    SEARCH_TITLE_TEXT = (By.XPATH, "//*[@data-id = '7e4a3e4']//div[1]//h1[1]")
    SEARCH_TRY_FREE_TEXT = (By.XPATH, "//*[@data-id = '68c810c4']//div[1]//h2[1]")
    SELECT_FILE_BUTTON = (By.ID, "dl_flip2pdf_uploaded_file")
    TERMS_AND_CONDITIONS_CHECKBOX = (By.ID, "dl_flip2pdf_disclaimer_check")
    SUBMIT_BUTTON = (By.ID, "dl_flip2pdf_submit_btn")
    PROCESSING_MESSAGE = (By.ID, "dl_flip2pdf_processing_msg")
    DOWNLOAD_REPORT_LINK = (By.ID, "dl_flip2pdf_download_link")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_title_phrase(self, phrase):
        return self.browser.find_element(*self.SEARCH_TITLE_TEXT)

    def search_try_free_phrase(self, phrase):
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