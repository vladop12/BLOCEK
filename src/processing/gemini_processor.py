"""
Modul pre spracovanie pokladničných blokov pomocou Google Gemini API.
Poskytuje funkcie pre rozpoznávanie textu a extrakciu údajov z obrázkov.
"""

import os
import base64
import json
import requests
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class GeminiProcessor:
    """
    Trieda pre spracovanie obrázkov pomocou Google Gemini API.
    """
    
    def __init__(self, api_key=None):
        """
        Inicializácia procesora pre Gemini API.
        
        Args:
            api_key (str, optional): API kľúč pre Google Gemini. 
                Ak nie je zadaný, pokúsi sa ho načítať z premennej prostredia GEMINI_API_KEY.
        """
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            logger.warning("API kľúč pre Gemini nie je nastavený. Použite environment premennú GEMINI_API_KEY alebo zadajte kľúč pri inicializácii.")
        
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"
    
    def _encode_image(self, image_path):
        """
        Zakóduje obrázok do base64 formátu pre API.
        
        Args:
            image_path (str): Cesta k obrázku.
            
        Returns:
            str: Base64 zakódovaný obrázok.
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def process_receipt(self, image_path):
        """
        Spracovanie obrázku pokladničného bloku a extrakcia údajov.
        
        Args:
            image_path (str): Cesta k obrázku.
            
        Returns:
            dict: Extrahované údaje z pokladničného bloku.
        """
        if not self.api_key:
            logger.error("API kľúč pre Gemini nie je nastavený.")
            return {"error": "API kľúč nie je nastavený"}
        
        try:
            # Zakódovanie obrázku
            image_data = self._encode_image(image_path)
            
            # Vytvorenie požiadavky pre API
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": """
                                Analyzuj tento pokladničný blok a extrahuj nasledujúce informácie v JSON formáte:
                                - názov obchodu
                                - dátum nákupu (vo formáte DD.MM.YYYY)
                                - čas nákupu
                                - celková suma
                                - zoznam položiek (názov, množstvo, jednotková cena, celková cena)
                                - DPH (rozdelené podľa sadzieb)
                                
                                Vráť len JSON bez ďalšieho textu.
                                """
                            },
                            {
                                "inline_data": {
                                    "mime_type": f"image/{Path(image_path).suffix[1:]}",
                                    "data": image_data
                                }
                            }
                        ]
                    }
                ]
            }
            
            # Odoslanie požiadavky na API
            response = requests.post(
                f"{self.api_url}?key={self.api_key}",
                json=payload
            )
            
            # Spracovanie odpovede
            if response.status_code == 200:
                response_data = response.json()
                # Extrakcia JSON z odpovede
                text_response = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")
                
                # Pokus o parsovanie JSON
                try:
                    return json.loads(text_response)
                except json.JSONDecodeError:
                    logger.error(f"Nepodarilo sa parsovať JSON z odpovede: {text_response}")
                    return {"error": "Nepodarilo sa parsovať JSON z odpovede", "raw_response": text_response}
            else:
                logger.error(f"Chyba pri komunikácii s API: {response.status_code} - {response.text}")
                return {"error": f"Chyba pri komunikácii s API: {response.status_code}", "details": response.text}
                
        except Exception as e:
            logger.exception(f"Nastala chyba pri spracovaní bloku: {e}")
            return {"error": f"Nastala chyba pri spracovaní bloku: {str(e)}"}
    
    def process_multiple_receipts(self, image_paths):
        """
        Spracovanie viacerých pokladničných blokov.
        
        Args:
            image_paths (list): Zoznam ciest k obrázkom.
            
        Returns:
            list: Zoznam extrahovaných údajov z pokladničných blokov.
        """
        results = []
        for image_path in image_paths:
            logger.info(f"Spracovávam blok: {image_path}")
            result = self.process_receipt(image_path)
            result["source_image"] = image_path
            results.append(result)
        
        return results
