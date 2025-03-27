"""
Modul pre spracovanie pokladničných blokov pomocou Google Gemini API.
"""

import json
import logging
import os
from pathlib import Path
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

class GeminiProcessor:
    """
    Trieda pre spracovanie pokladničných blokov pomocou Google Gemini API.
    """
    
    def __init__(self, api_key):
        """
        Inicializácia procesora.
        
        Args:
            api_key (str): API kľúč pre Google Gemini API.
        """
        self.api_key = api_key
        # Inicializácia klienta
        self.client = genai.Client(api_key=self.api_key)
        
        # Použitie modelu gemini-2.0-flash pre prácu s obrázkami
        self.model_name = "gemini-2.0-flash"
        
    def process_receipt(self, image_path):
        """
        Spracuje pokladničný blok pomocou Google Gemini API.
        
        Args:
            image_path (str): Cesta k obrázku pokladničného bloku.
            
        Returns:
            dict: Spracované údaje z pokladničného bloku.
        """
        try:
            # Načítanie obrázku ako bytes
            image_bytes = Path(image_path).read_bytes()
            
            # Vytvorenie promptu
            prompt = """
            Analyzuj tento pokladničný blok a extrahuj nasledujúce informácie v JSON formáte:
            - názov obchodu
            - dátum nákupu
            - celková suma
            - jednotlivé položky (názov, množstvo, cena za kus, celková cena)
            
            Vráť len JSON bez ďalšieho textu.
            """
            
            # Vytvorenie obsahu s použitím types.Content a types.Part
            content = types.Content(
                parts=[
                    types.Part(text=prompt),
                    types.Part(
                        inline_data=types.Blob(
                            mime_type="image/jpeg",
                            data=image_bytes
                        )
                    )
                ]
            )
            
            # Odoslanie požiadavky na API
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=content
            )
            
            # Spracovanie odpovede
            text = response.text
            
            # Pokus o parsovanie JSON
            try:
                # Nájdenie JSON v texte (pre prípad, že API vráti aj iný text)
                import re
                json_match = re.search(r'({.*})', text, re.DOTALL)
                if json_match:
                    text = json_match.group(1)
                
                result = json.loads(text)
                return result
            except json.JSONDecodeError as e:
                logger.error(f"Chyba pri parsovaní JSON: {e}")
                return {
                    "error": "Chyba pri parsovaní JSON",
                    "details": str(e),
                    "raw_text": text
                }
                
        except Exception as e:
            logger.exception(f"Neočakávaná chyba pri spracovaní pokladničného bloku: {e}")
            return {
                "error": "Neočakávaná chyba pri spracovaní",
                "details": str(e)
            }
