"""
Demonštračný skript pre spracovanie pokladničných blokov pomocou Google Gemini API.
"""

import os
import sys
import json
from pathlib import Path

# Pridanie koreňového adresára projektu do sys.path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.processing.gemini_processor import GeminiProcessor
from src.utils.env_loader import load_env_file

def main():
    """Hlavná funkcia pre demonštráciu spracovania pokladničných blokov."""
    # Načítanie premenných prostredia
    load_env_file()
    
    # Kontrola, či je nastavený API kľúč
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Chyba: GEMINI_API_KEY nie je nastavený v .env súbore")
        return
    
    # Inicializácia procesora
    try:
        processor = GeminiProcessor(api_key=api_key)
    except Exception as e:
        print(f"Chyba pri inicializácii procesora: {e}")
        return
    
    # Cesta k testovaciemu obrázku
    test_image_path = Path(project_root) / "resources" / "test_receipt.jpg"
    
    # Kontrola, či testovací obrázok existuje
    if not test_image_path.exists():
        print(f"Chyba: Testovací obrázok neexistuje: {test_image_path}")
        return
    
    print(f"Spracovávam pokladničný blok: {test_image_path}")
    print(f"Používam model: {processor.model_name}")
    print("Čakajte prosím, spracovanie môže trvať niekoľko sekúnd...")
    
    # Spracovanie pokladničného bloku
    result = processor.process_receipt(str(test_image_path))
    
    # Kontrola, či výsledok obsahuje chybu
    if "error" in result:
        print(f"\nChyba pri spracovaní: {result['error']}")
        if "details" in result:
            print(f"Detaily: {result['details']}")
        if "raw_text" in result:
            print(f"\nSurový text z API:\n{result['raw_text']}")
        return
    
    # Výpis výsledku
    print("\nVýsledok spracovania:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Výpis jednotlivých položiek, ak existujú
    if "jednotlivé položky" in result:
        print("\nZoznam položiek:")
        for i, item in enumerate(result["jednotlivé položky"], 1):
            print(f"{i}. {item.get('názov', 'Neznámy názov')} - "
                  f"{item.get('množstvo', '1')} x "
                  f"{item.get('cena za kus', 'N/A')} = "
                  f"{item.get('celková cena', 'N/A')}")

if __name__ == "__main__":
    main()
