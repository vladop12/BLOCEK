"""
Testovací skript pre overenie funkčnosti Google Gemini API s obrázkami.
"""

from google import genai
from google.genai import types
from pathlib import Path
import sys

def test_vision_api(image_path):
    """Test funkcionality API pre prácu s obrázkami."""
    try:
        # Inicializácia klienta s API kľúčom
        api_key = "AIzaSyAsprkYRP3oXxyY-Qcxhz6qYH70HL0Gvjw"
        client = genai.Client(api_key=api_key)
        
        print(f"Načítavam obrázok: {image_path}")
        # Načítanie obrázka ako bytes
        image_bytes = Path(image_path).read_bytes()
        
        # Vytvorenie obsahu s použitím types.Content a types.Part
        content = types.Content(
            parts=[
                types.Part(text="Popíš, čo vidíš na tomto obrázku."),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=image_bytes
                    )
                )
            ]
        )
        
        # Odoslanie požiadavky na API
        print("Odosielam požiadavku na API...")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=content
        )
        
        print("\nOdpoveď API:")
        print(response.text)
        
        print("\nTest úspešný! API pre obrázky je funkčné.")
        return True
        
    except Exception as e:
        print(f"\nCHYBA pri testovaní API pre obrázky: {e}")
        print(f"Typ chyby: {type(e).__name__}")
        print(f"Detaily: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== Test Google Gemini API pre obrázky ===\n")
    
    # Cesta k testovaciemu obrázku
    test_image = "resources/test_receipt.jpg"
    
    success = test_vision_api(test_image)
    sys.exit(0 if success else 1)
