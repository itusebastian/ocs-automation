"""
Module: classifier.py
Description: Classify communications by type using NLP (spaCy) for OCS automation system.
Best practices: Use pre-trained models, allow for rule-based and ML-based classification, log actions, and handle errors.
"""
import spacy
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

try:
    nlp = spacy.load('es_core_news_md')  # Spanish model
except Exception as e:
    logging.error(f"spaCy model not found: {e}. Please install 'es_core_news_md'.")
    nlp = None

PROCESS_TYPES = [
    'homologación',
    'titulación',
    'convalidación',
    'apelaciones',
    'becas',
    'otro'
]

def classify_text(text: str) -> Optional[str]:
    """Classify communication type based on keywords and NLP."""
    if not nlp:
        logging.error("spaCy model not loaded.")
        return None
    doc = nlp(text)
    text_lower = text.lower()
    for process in PROCESS_TYPES:
        if process in text_lower:
            logging.info(f"Classified as: {process}")
            return process
    # Fallback: use entity recognition or ML model here
    logging.info("Classified as: otro")
    return 'otro'

if __name__ == "__main__":
    sample_text = "Solicitud de homologación de materias para el estudiante Juan Pérez."
    print(classify_text(sample_text))
