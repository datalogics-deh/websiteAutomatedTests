from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.remote import webelement


class ProductPdfAlchemistPage:
    URL = 'https://www.datalogics.com/products/pdf-tools/pdf-alchemist/'
    SEARCH_TITLE_TEXT = (By.XPATH, "//*[@data-id = '22b90105']//div[1]//h1[1]")
    SEARCH_TRY_FREE_TEXT = (By.XPATH, "//*[@data-id = '1b4a2386']//div[1]//h2[1]")
    SELECT_FILE_BUTTON = (By.ID, "dl_pdfalchemist_uploaded_file")
    OUTPUT_FORMAT_DROPDOWN = (By.ID, "dl_outputFormat")
    TERMS_AND_CONDITIONS_CHECKBOX = (By.ID, "dl_pdfalchemist_disclaimer_check")
    SUBMIT_BUTTON = (By.ID, "dl_pdfalchemist_submit_btn")
    PROCESSING_MESSAGE = (By.ID, "dl_pdfalchemist_processing_msg")
    DOWNLOAD_REPORT_LINK = (By.ID, "dl_pdfalchemist_download_link")
    FIRST_PAGE_ONLY_CHECKBOX = (By.NAME, "firstPage")
    ONLY_EXTRACT_TABLES_CHECKBOX = (By.NAME, "tablesOnly")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_title_phrase(self):
        return self.browser.find_element(*self.SEARCH_TITLE_TEXT)

    def get_try_free_phrase(self):
        return self.browser.find_element(*self.SEARCH_TRY_FREE_TEXT)

    def select_file(self, file):
        self.browser.find_element(*self.SELECT_FILE_BUTTON).send_keys(file)

    def select_output_format_dropdown(self, output_format):
        selector = ui.Select(self.browser.find_element(*self.OUTPUT_FORMAT_DROPDOWN))
        selector.select_by_visible_text(output_format)

    def uncheck_first_page_only_checkbox(self):
        self.browser.find_element(*self.FIRST_PAGE_ONLY_CHECKBOX).click()

    def check_only_extract_tables_checkbox(self):
        self.browser.find_element(*self.ONLY_EXTRACT_TABLES_CHECKBOX).click()

    def click_terms_and_conditions_checkbox(self):
        self.browser.find_element(*self.TERMS_AND_CONDITIONS_CHECKBOX).click()

    def click_submit_button(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def wait_on_processing_message_to_be_present(self, TIME):
        ui.WebDriverWait(self.browser, TIME).until(expected_conditions.presence_of_element_located(self.PROCESSING_MESSAGE))

    def wait_on_processing_message_to_disappear(self, TIME):
        ui.WebDriverWait(self.browser, TIME).until(expected_conditions.invisibility_of_element_located(self.PROCESSING_MESSAGE))

    def verify_download_report(self):
        if len(self.browser.find_elements(*self.DOWNLOAD_REPORT_LINK)) > 0:
            return True
        else:
            return False