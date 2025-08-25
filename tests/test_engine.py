"""
Test: test_engine.py
Purpose: Unit test for process_communication function in engine.py
Best practices: Test all decision branches and edge cases.
"""
import unittest
from src.decision_engine.engine import process_communication

class TestDecisionEngine(unittest.TestCase):
    def setUp(self):
        self.valid_info = {'student_id': '12345', 'subject': 'Matemáticas'}
        self.missing_info = {'student_id': '', 'subject': ''}

    def test_request_missing_info(self):
        result = process_communication(self.missing_info, 'homologación', 0.95)
        self.assertEqual(result, 'request_missing_info')

    def test_low_confidence(self):
        result = process_communication(self.valid_info, 'homologación', 0.5)
        self.assertEqual(result, 'manual_review')

    def test_generate_resolution(self):
        result = process_communication(self.valid_info, 'homologación', 0.95)
        self.assertEqual(result, 'generate_resolution')

    def test_notify_titulacion(self):
        result = process_communication(self.valid_info, 'titulación', 0.95)
        self.assertEqual(result, 'notify_titulacion_department')

    def test_notify_convalidacion(self):
        result = process_communication(self.valid_info, 'convalidación', 0.95)
        self.assertEqual(result, 'notify_convalidacion_department')

    def test_manual_review_apelaciones(self):
        result = process_communication(self.valid_info, 'apelaciones', 0.95)
        self.assertEqual(result, 'manual_review')

    def test_notify_scholarships(self):
        result = process_communication(self.valid_info, 'becas', 0.95)
        self.assertEqual(result, 'notify_scholarships_department')

    def test_other(self):
        result = process_communication(self.valid_info, 'otro', 0.95)
        self.assertEqual(result, 'manual_review')

if __name__ == "__main__":
    unittest.main()
