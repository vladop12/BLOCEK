# BLOCEK
Automatizovaný systém na spracovanie pokladničných blokov pomocou AI modelu Gemini.

## Popis

BLOCEK je aplikácia na automatizáciu procesu extrakcie údajov z pokladničných blokov uložených vo zvolenom adresári. Aplikácia umožňuje:
- Manuálny výber adresára s pokladničnými blokmi
- Extrakciu údajov z pokladničných blokov pomocou AI modelu Gemini
- Ukladanie extrahovaných údajov do Excel súborov
- Generovanie XML súborov na základe extrahovaných údajov

## Inštalácia

1. Klonujte repozitár:
```
git clone https://github.com/yourusername/BLOCEK.git
cd BLOCEK
```

2. Nainštalujte závislosti:
```
pip install -r requirements.txt
```

3. Nastavte API kľúč pre Gemini API v súbore config.py alebo ako premennú prostredia:
```
export GEMINI_API_KEY="váš_api_kľúč"
```

## Použitie

1. Spustite aplikáciu:
```
python main.py
```

2. Vyberte adresár s pokladničnými blokmi pomocou tlačidla "Prehľadávať..."
3. Vyberte súbory, ktoré chcete spracovať
4. Kliknite na tlačidlo "Spracovať vybrané súbory"
5. Extrahované údaje sa uložia do Excel súboru
6. Pre generovanie XML súborov kliknite na tlačidlo "Generovať XML"

## Podporované formáty súborov

- Obrázky: .jpg, .jpeg, .png
- Dokumenty: .pdf

## Licencia

Tento projekt je licencovaný pod [MIT licenciou](LICENSE).
```