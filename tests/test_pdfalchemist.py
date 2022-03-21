import pytest, os
from webpages.pdftools_pdfalchemist import ProductPdfAlchemistPage
import time

TITLE_PHRASE = 'PDF Alchemist ™'
TRY_FREE_PHRASE = 'Try the Free Demo'
TEST_DIR = os.path.join(os.getcwd(), "tests", "samples", "pdfalchemist")
TEST_FILE = os.path.join(TEST_DIR, "basic.pdf")


def test_basic_pdfalchemist_load_page(browser):
    webpage = ProductPdfAlchemistPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    assert webpage.get_try_free_phrase().text == TRY_FREE_PHRASE


def test_basic_pdfalchemist_output_html(browser):
    webpage = ProductPdfAlchemistPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("HTML")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_pdfalchemist_output_xml(browser):
    webpage = ProductPdfAlchemistPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("XML")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_pdfalchemist_output_json(browser):
    webpage = ProductPdfAlchemistPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("JSON")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_pdfalchemist_process_all_pages(browser):
    all_pages_file = os.path.join(TEST_DIR, "080_Formal_Grammars.pdf")
    webpage = ProductPdfAlchemistPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(all_pages_file)
    webpage.select_output_format_dropdown("JSON")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    time.sleep(5)
    assert webpage.verify_download_report() == True


def test_basic_pdfalchemist_process_only_tables(browser):
    only_tables_file = os.path.join(TEST_DIR, "Table-emptycell-1.pdf")
    webpage = ProductPdfAlchemistPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(only_tables_file)
    webpage.select_output_format_dropdown("JSON")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True