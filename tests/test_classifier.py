"""
Test: test_classifier.py
Purpose: Unit test for classify_text function in classifier.py
Best practices: Use sample texts for each process type and check correct classification.
"""
import unittest
from src.nlp.classifier import classify_text

class TestClassifier(unittest.TestCase):
    def test_homologacion(self):
        text = "Solicitud de homologación de materias para el estudiante."
        self.assertEqual(classify_text(text), 'homologación')

    def test_titulacion(self):
        text = "Proceso de titulación para el estudiante."
        self.assertEqual(classify_text(text), 'titulación')

    def test_convalidacion(self):
        text = "Petición de convalidación de asignaturas."
        self.assertEqual(classify_text(text), 'convalidación')

    def test_apelaciones(self):
        text = "Apelaciones sobre la resolución emitida."
        self.assertEqual(classify_text(text), 'apelaciones')

    def test_becas(self):
        text = "Solicitud de becas para el próximo ciclo."
        self.assertEqual(classify_text(text), 'becas')

    def test_otro(self):
        text = "Consulta general sobre horarios."
        self.assertEqual(classify_text(text), 'otro')

if __name__ == "__main__":
    unittest.main()
