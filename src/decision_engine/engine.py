"""
Module: engine.py
Description: Decision engine for OCS automation system. Determines workflow actions based on extracted info, classification, and confidence.
Best practices: Use clear rules, log decisions, handle errors, and allow for easy extension.
"""
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

CONFIDENCE_THRESHOLD = 0.8

# Example decision rules
# info: dict with extracted fields (student_id, subject, etc.)
# classification: string from classifier
# confidence: float from NLP model (if available)
def process_communication(info: Dict[str, Any], classification: str, confidence: float) -> str:
    """Decide next action for a communication."""
    if not info.get('student_id') or not info.get('subject'):
        logging.info('Missing required info: requesting more information.')
        return 'request_missing_info'
    if confidence < CONFIDENCE_THRESHOLD:
        logging.info('Low confidence: marking for manual review.')
        return 'manual_review'
    if classification == 'homologación':
        logging.info('Homologación: generating resolution.')
        return 'generate_resolution'
    if classification == 'titulación':
        logging.info('Titulación: notifying titulación department.')
        return 'notify_titulacion_department'
    if classification == 'convalidación':
        logging.info('Convalidación: notifying convalidación department.')
        return 'notify_convalidacion_department'
    if classification == 'apelaciones':
        logging.info('Apelaciones: marking for review by services department.')
        return 'manual_review'
    if classification == 'becas':
        logging.info('Becas: notifying scholarships department.')
        return 'notify_scholarships_department'
    logging.info('Other: marking for manual review.')
    return 'manual_review'

if __name__ == "__main__":
    # Example usage
    info = {'student_id': '12345', 'subject': 'Matemáticas'}
    print(process_communication(info, 'homologación', 0.95))
    print(process_communication({}, 'titulación', 0.95))
    print(process_communication(info, 'apelaciones', 0.7))
