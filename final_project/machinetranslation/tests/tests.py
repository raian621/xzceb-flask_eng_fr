import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
    # None input tests
    def test_e2f_none(self):
        self.assertIsNone(english_to_french(None))
    def test_f2e_none(self):
        self.assertIsNone(french_to_english(None))
    
    # English to French tests
    def test_e2f_equal(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_e2f_unequal(self):
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')
    
    # French to English tests
    def test_f2e_equal(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_f2e_unequal(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodbye')

unittest.main()