import pytest, os
from webpages.pdftools_flip2pdf import ProductFlip2PdfPage

TITLE_PHRASE = 'FLIP2PDF ™'
TRY_FREE_PHRASE = 'Try the Free Demo'
TEST_DIR = os.path.join(os.getcwd(), "tests", "samples", "flip2pdf")


def test_basic_flip2pdf_load_page(browser):
    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    assert webpage.search_try_free_phrase().text == TRY_FREE_PHRASE


def test_basic_flip2pdf_process_bmp(browser):
    test_file = os.path.join(TEST_DIR, "ducky.bmp")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_jpg(browser):
    test_file = os.path.join(TEST_DIR, "ducky.jpg")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_png(browser):
    test_file = os.path.join(TEST_DIR, "ducky.png")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_tif(browser):
    test_file = os.path.join(TEST_DIR, "ducky.tif")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_xls(browser):
    test_file = os.path.join(TEST_DIR, "excelxls.xls")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_xlsx(browser):
    test_file = os.path.join(TEST_DIR, "excelxlsx.xlsx")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_ppt(browser):
    test_file = os.path.join(TEST_DIR, "powerpointppt.ppt")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_pptx(browser):
    test_file = os.path.join(TEST_DIR, "powerpointppt.ppt")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_eps(browser):
    test_file = os.path.join(TEST_DIR, "STD-EPS_sample.eps")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_ps(browser):
    test_file = os.path.join(TEST_DIR, "STD-PS_sample.ps")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_doc(browser):
    test_file = os.path.join(TEST_DIR, "worddocstandard.doc")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True


def test_basic_flip2pdf_process_docx(browser):
    test_file = os.path.join(TEST_DIR, "worddocx.docx")

    webpage = ProductFlip2PdfPage(browser)
    webpage.load()
    assert webpage.search_title_phrase().text == TITLE_PHRASE
    webpage.select_file(test_file)
    webpage.click_terms_and_conditions_checkbox()
    webpage.click_submit_button()
    webpage.wait_on_processing_message_to_be_present(5)
    webpage.wait_on_processing_message_to_disappear(30)
    assert webpage.verify_download_report() == True
