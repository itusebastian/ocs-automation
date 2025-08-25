"""
demo.py
Purpose: Run an end-to-end demo of the OCS automation MVP using sample data.
"""
import os
from src.ingestion.doc_ingest import extract_text_from_pdf, extract_text_from_image
from src.nlp.classifier import classify_text
from src.decision_engine.engine import process_communication

# Sample data paths (update as needed)
pdf_path = 'data/sample.pdf'
image_path = 'data/sample_image.jpeg'

# Simulate extracted info from email (in real use, parse email)
info = {
    'student_id': '12345',
    'subject': 'Matemáticas'
}

# Step 1: Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)
print(f"Extracted PDF text: {pdf_text}")

# Step 2: Extract text from image
image_text = extract_text_from_image(image_path)
print(f"Extracted image text: {image_text}")

# Step 3: Classify communication type (using PDF text as example)
classification = classify_text(pdf_text or "")
print(f"Classification: {classification}")

# Step 4: Simulate confidence (for demo, set to 0.95 if text found, else 0.5)
confidence = 0.95 if pdf_text else 0.5

# Step 5: Decision engine
action = process_communication(info, classification, confidence)
print(f"Decision engine action: {action}")

# Step 6: Summary
print("\nDemo complete. You can now extend this script to process real emails and documents.")
