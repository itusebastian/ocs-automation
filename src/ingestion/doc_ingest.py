"""
Module: doc_ingest.py
Description: Extract text from PDFs and scanned images using OCR for OCS automation system.
Best practices: Use modular functions, handle errors, log actions, and support multiple formats.
"""
import os
import logging
from typing import Optional

try:
    import pdf2image
    from PIL import Image
    import pytesseract
except ImportError:
    raise ImportError("Please install pdf2image, Pillow, and pytesseract for document extraction.")

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def extract_text_from_pdf(pdf_path: str) -> Optional[str]:
    """Extract text from a PDF using OCR."""
    try:
        images = pdf2image.convert_from_path(pdf_path)
        text = ''
        for img in images:
            text += pytesseract.image_to_string(img)
        logging.info(f'Text extracted from PDF: {pdf_path}')
        return text
    except Exception as e:
        logging.error(f'Error extracting text from PDF {pdf_path}: {e}')
        return None

def extract_text_from_image(image_path: str) -> Optional[str]:
    """Extract text from an image using OCR."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        logging.info(f'Text extracted from image: {image_path}')
        return text
    except Exception as e:
        logging.error(f'Error extracting text from image {image_path}: {e}')
        return None

if __name__ == "__main__":
    # Example usage
    pdf_file = 'data/sample.pdf'
    image_file = 'data/sample_image.png'
    print(extract_text_from_pdf(pdf_file))
    print(extract_text_from_image(image_file))
