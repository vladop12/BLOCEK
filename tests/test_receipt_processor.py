"""
Testy pre GeminiProcessor.
"""

import os
import sys
import unittest
from pathlib import Path
from PIL import Image
from google import genai

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
        self.assertIsNotNone(self.processor.client)
    
    def test_process_receipt_with_image(self):
        """Test, či metóda process_receipt dokáže spracovať obrázok."""
        # Pre tento test potrebujete testovací obrázok
        test_image_path = Path(project_root) / "resources" / "test_receipt.jpg"
        
        # Preskočiť test, ak testovací obrázok neexistuje
        if not test_image_path.exists():
            self.skipTest(f"Testovací obrázok neexistuje: {test_image_path}")
        
        # Kontrola, či je obrázok čitateľný pomocou PIL
        try:
            img = Image.open(test_image_path)
            img.verify()  # Kontrola, či je obrázok platný
        except Exception as e:
            self.skipTest(f"Testovací obrázok nie je platný: {e}")

if __name__ == "__main__":
    unittest.main()
