import pytest, os
from webpages.pdftools_pdf2img import ProductPdf2ImgPage

TITLE_PHRASE = 'PDF2IMG ™'
TRY_FREE_PHRASE = 'Try the Free Demo'
TEST_DIR = os.path.join(os.getcwd(), "tests", "samples", "pdf2img")
TEST_FILE = os.path.join(TEST_DIR, "basic.pdf")


def test_basic_pdf2img_load_page(browser):
    webpage = ProductPdf2ImgPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    assert webpage.get_try_free_phrase().text == TRY_FREE_PHRASE


def test_basic_pdf2img_output_png(browser):
    webpage = ProductPdf2ImgPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("PNG")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True

def test_basic_pdf2img_output_jpg(browser):
    webpage = ProductPdf2ImgPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("JPG")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True

def test_basic_pdf2img_output_gif(browser):
    webpage = ProductPdf2ImgPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("GIF")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True

def test_basic_pdf2img_output_tif(browser):
    webpage = ProductPdf2ImgPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("TIF")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True

def test_basic_pdf2img_output_bmp(browser):
    webpage = ProductPdf2ImgPage(browser)
    webpage.load()
    assert webpage.get_title_phrase().text == TITLE_PHRASE
    webpage.select_file(TEST_FILE)
    webpage.select_output_format_dropdown("BMP")
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True
