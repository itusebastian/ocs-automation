"""
Test: test_doc_ingest.py
Purpose: Unit test for document extraction functions in doc_ingest.py
Best practices: Use sample files and mock OCR for fast, reliable tests.
"""
import unittest
from unittest.mock import patch, MagicMock
from src.ingestion import doc_ingest

class TestDocIngest(unittest.TestCase):
    @patch('src.ingestion.doc_ingest.pytesseract.image_to_string')
    @patch('src.ingestion.doc_ingest.pdf2image.convert_from_path')
    def test_extract_text_from_pdf(self, mock_convert, mock_ocr):
        # Mock image and OCR output
        mock_img = MagicMock()
        mock_convert.return_value = [mock_img]
        mock_ocr.return_value = 'Texto extraído'
        text = doc_ingest.extract_text_from_pdf('dummy.pdf')
        self.assertEqual(text, 'Texto extraído')

    @patch('src.ingestion.doc_ingest.pytesseract.image_to_string')
    @patch('src.ingestion.doc_ingest.Image.open')
    def test_extract_text_from_image(self, mock_open, mock_ocr):
        mock_img = MagicMock()
        mock_open.return_value = mock_img
        mock_ocr.return_value = 'Texto imagen'
        text = doc_ingest.extract_text_from_image('dummy.png')
        self.assertEqual(text, 'Texto imagen')

if __name__ == "__main__":
    unittest.main()
