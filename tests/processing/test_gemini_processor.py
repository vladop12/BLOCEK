"""
Testy pre GeminiProcessor.
"""

import os
import sys
import unittest
from pathlib import Path

# Pridanie koreňového adresára projektu do sys.path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.processing.gemini_processor import GeminiProcessor
from src.utils.env_loader import load_env_file

class TestGeminiProcessor(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Načítanie premenných prostredia pred testami
        load_env_file()
        
        # Kontrola, či je nastavený API kľúč
        cls.api_key = os.environ.get("GEMINI_API_KEY")
        if not cls.api_key:
            raise unittest.SkipTest("GEMINI_API_KEY nie je nastavený v .env súbore")
    
    def setUp(self):
        self.processor = GeminiProcessor(api_key=self.api_key)
    
    def test_initialization(self):
        """Test, či sa GeminiProcessor správne inicializuje."""
        self.assertIsNotNone(self.processor)
        self.assertEqual(self.processor.api_key, self.api_key)
    
    def test_encode_image(self):
        """Test, či metóda _encode_image funguje správne."""
        # Pre tento test potrebujete testovací obrázok
        test_image_path = Path(project_root) / "resources" / "test_receipt.jpg"
        
        # Preskočiť test, ak testovací obrázok neexistuje
        if not test_image_path.exists():
            self.skipTest(f"Testovací obrázok neexistuje: {test_image_path}")
        
        encoded_image = self.processor._encode_image(str(test_image_path))
        self.assertIsNotNone(encoded_image)
        self.assertIsInstance(encoded_image, str)
        self.assertTrue(len(encoded_image) > 0)
    def test_process_receipt(self):
        """Test spracovania pokladničného bloku."""
        # Pre tento test potrebujete testovací obrázok
        test_image_path = Path(project_root) / "resources" / "test_receipt.jpg"
    
        # Preskočiť test, ak testovací obrázok neexistuje
        if not test_image_path.exists():
            self.skipTest(f"Testovací obrázok neexistuje: {test_image_path}")
    
        # Spracovanie pokladničného bloku
        result = self.processor.process_receipt(str(test_image_path))
    
        # Kontrola výsledku
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
    
        # Kontrola, či výsledok neobsahuje chybu
        self.assertNotIn('error', result, f"Spracovanie zlyhalo s chybou: {result.get('error', '')}")
    
        # Kontrola, či výsledok obsahuje očakávané kľúče
        expected_keys = ['názov obchodu', 'dátum nákupu', 'celková suma']
        for key in expected_keys:
            self.assertIn(key, result, f"Výsledok neobsahuje očakávaný kľúč: {key}")
   

if __name__ == "__main__":
    unittest.main()
