import pytest, os
from webpages.pdftools_pdfformsflattener import ProductFormsFlattenerPage

TITLE_PHRASE = 'PDF Forms Flattener™'
TRY_FREE_PHRASE = 'Try The Free Demo'
TEST_DIR = os.path.join(os.getcwd(), "tests", "samples", "pdfformsflattener")
TEST_FILE = os.path.join(TEST_DIR, "example_acroform.pdf")


def test_basic_forms_flattener_load_page(browser):
    webpage = ProductFormsFlattenerPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    assert webpage.search_try_free_phrase().text == TRY_FREE_PHRASE


def test_basic_forms_flattener_process_pdf(browser):
    webpage = ProductFormsFlattenerPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True
