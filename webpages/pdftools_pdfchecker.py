import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from pywinauto import Application


class ProductPdfCheckerPage:
    URL = 'https://www.datalogics.com/products/pdf-tools/pdf-checker/'
    SEARCH_TITLE_TEXT = (By.XPATH, "//*[@id = 'pdf-checker-h1']//div[1]//h1[1]")
    SEARCH_TRY_FREE_TEXT = (By.XPATH, "//*[@data-id = '650cae71']//div[1]//h2[1]")
    SELECT_FILE_BUTTON = (By.ID, "dl_pdfchecker_upload_button")
    OUTPUT_FORMAT_DROPDOWN = (By.ID, "outType")
    TERMS_AND_CONDITIONS_CHECKBOX = (By.ID, "dl_pdfchecker_disclaimer_check")
    SUBMIT_BUTTON = (By.ID, "dl_pdfchecker_submit_btn")
    DOWNLOAD_REPORT_LINK = (By.ID, "dl_pdfchecker_download_link")
    PROCESSING_MESSAGE = (By.ID, "dl_pdfchecker_processing_message")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_title_phrase(self):
        return self.browser.find_element(*self.SEARCH_TITLE_TEXT)

    def search_try_free_phrase(self):
        return self.browser.find_element(*self.SEARCH_TRY_FREE_TEXT)

    def select_file(self, file):
        self.browser.find_element(*self.SELECT_FILE_BUTTON).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title='Open')
        app.Open.type_keys(file)
        app.Open.OpenButton.click_input()

    def select_output_format_dropdown(self, format):
        selector = ui.Select(self.browser.find_element(*self.OUTPUT_FORMAT_DROPDOWN))
        selector.select_by_visible_text(format)

    def click_terms_and_conditions_checkbox(self):
        self.browser.find_element(*self.TERMS_AND_CONDITIONS_CHECKBOX).click()

    def click_submit_button(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def wait_on_processing(self, wait_on_processing_time):
        ui.WebDriverWait(self.browser, wait_on_processing_time).until(expected_conditions.invisibility_of_element_located((self.PROCESSING_MESSAGE)))

    def verify_download_report(self):
        if len(self.browser.find_elements(*self.DOWNLOAD_REPORT_LINK)) > 0:
            return True
        else:
            return False