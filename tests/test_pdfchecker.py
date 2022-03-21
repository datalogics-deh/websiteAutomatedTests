import pytest, os
from webpages.pdftools_pdfchecker import ProductPdfCheckerPage

TITLE_PHRASE = 'PDF Checker ™'
TRY_FREE_PHRASE = 'Try PDF Checker Free Online'
TEST_DIR = os.path.join(os.getcwd(), "tests", "samples", "pdfchecker")


def test_basic_pdfchecker_load_page(browser):

    checker_page = ProductPdfCheckerPage(browser)
    checker_page.load()
    assert checker_page.search_title_phrase().text == TITLE_PHRASE
    assert checker_page.search_try_free_phrase().text == TRY_FREE_PHRASE


def test_basic_pdfchecker_process_pdf_json_output(browser):
    output_format = 'JSON'
    test_file = os.path.join(TEST_DIR, "basic.pdf")

    checker_page = ProductPdfCheckerPage(browser)
    checker_page.load()
    assert checker_page.search_title_phrase().text == TITLE_PHRASE
    checker_page.select_file(test_file)
    checker_page.select_output_format_dropdown(output_format)
    checker_page.click_terms_and_conditions_checkbox()
    checker_page.click_submit_button()
    checker_page.wait_on_processing(3)
    assert checker_page.verify_download_report() == True


def test_basic_pdfchecker_process_pdf_text_output(browser):
    output_format = 'Text'
    test_file = os.path.join(TEST_DIR, "basic.pdf")

    checker_page = ProductPdfCheckerPage(browser)
    checker_page.load()
    assert checker_page.search_title_phrase().text == TITLE_PHRASE
    checker_page.select_file(test_file)
    checker_page.select_output_format_dropdown(output_format)
    checker_page.click_terms_and_conditions_checkbox()
    checker_page.click_submit_button()
    checker_page.wait_on_processing(3)
    assert checker_page.verify_download_report() == True
