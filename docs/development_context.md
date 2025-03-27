# Vývojový kontext projektu BLOCEK

## Prehľad projektu

BLOCEK je aplikácia určená na spracovanie pokladničných blokov. Umožňuje používateľom načítať obrázky pokladničných blokov, extrahovať z nich relevantné údaje a organizovať tieto údaje pre ďalšie použitie.

## Aktuálny stav (Marec 2025)

### Implementované funkcie:
- Základné používateľské rozhranie s možnosťou výberu adresára so súbormi
- Zobrazenie zoznamu vybraných súborov
- Základné možnosti spracovania
- Panel pre spustenie spracovania a sledovanie jeho priebehu
- Zobrazenie výsledkov spracovania
- Možnosť exportu výsledkov do Excel súboru
- Simulácia generovania XML výstupu

### Technický dlh:
- Odstránená funkcionalita náhľadu obrázkov (`ImagePreview`), ktorá bude potrebovať reimplementáciu
- Aktuálne je implementovaná len simulácia spracovania blokov, nie skutočné OCR
- Potreba implementácie skutočnej logiky pre extrakciu údajov z blokov

### Architektúra:
- Modulárny dizajn s oddelenými komponentmi pre rôzne časti UI
- Použitie Tkinter pre vytvorenie používateľského rozhrania
- Logovanie aktivít pre lepšie debugovanie
- Testovanie pomocou unittest s mock objektami

## Plánované rozšírenia

### Krátkodobé ciele:
- Implementácia spracovania blokov pomocou Google Gemini API
- Integrácia umelej inteligencie pre extrakciu údajov z blokov
- Pridanie podpory pre rôzne formáty pokladničných blokov
- Reimplementácia náhľadu obrázkov

### Dlhodobé ciele:
- Integrácia s účtovnými systémami
- Mobilná aplikácia pre skenovanie blokov
- Cloudové úložisko pre zdieľanie a zálohovanie dát
- Štatistické analýzy výdavkov
- Vylepšenie presnosti extrakcie údajov pomocou trénovania AI modelu na špecifických typoch blokov

## Technické detaily

### Použité technológie:
- Python 3.11+
- Tkinter pre GUI
- Google Gemini API pre OCR a extrakciu údajov
- Unittest pre testovanie
- Logging pre zaznamenávanie aktivít

### Štruktúra projektu:
- `src/` - zdrojový kód aplikácie
  - `ui/` - komponenty používateľského rozhrania
    - `main_window.py` - hlavné okno aplikácie
    - `directory_selector.py` - komponenta pre výber adresára
    - `file_list.py` - komponenta pre zobrazenie zoznamu súborov
    - `processing_options.py` - komponenta pre nastavenie možností spracovania
    - `processing_panel.py` - komponenta pre ovládanie spracovania
    - `results_viewer.py` - komponenta pre zobrazenie výsledkov
  - `processing/` - logika spracovania blokov
    - `gemini_processor.py` - integrácia s Google Gemini API (bude implementované)
    - `data_extractor.py` - extrakcia štruktúrovaných údajov (bude implementované)
  - `models/` - dátové modely (bude implementované)
  - `utils/` - pomocné funkcie a nástroje (bude implementované)
- `tests/` - testy
  - `ui/` - testy UI komponentov
    - `test_main_window.py` - testy pre hlavné okno
    - ďalšie testy pre UI komponenty (budú implementované)
  - `processing/` - testy logiky spracovania (bude implementované)
- `docs/` - dokumentácia
  - `development_context.md` - kontext vývoja projektu
- `resources/` - statické zdroje (ikony, obrázky, atď.) (bude implementované)

## Vývojový proces

- Vývoj prebieha na GitHub pomocou vetiev (branches)
- Každá nová funkcia alebo oprava je implementovaná v samostatnej vetve
- Zmeny sú začlenené do hlavnej vetvy pomocou Pull Requestov
- Testy sú spúšťané manuálne pred každým commitom

## Aktuálne výzvy a ďalšie kroky

1. **Implementácia Google Gemini API**:
   - Vytvorenie a konfigurácia Google Cloud projektu
   - Získanie API kľúčov pre Gemini API
   - Implementácia klienta pre komunikáciu s API
   - Optimalizácia požiadaviek pre dosiahnutie najlepších výsledkov

2. **Extrakcia údajov pomocou AI**:
   - Definovanie štruktúry pre extrahované údaje
   - Vytvorenie promptov pre Gemini API na extrakciu špecifických údajov
   - Implementácia parsera pre spracovanie odpovedí z API
   - Riešenie problémov s nejednoznačnosťou a chybami v rozpoznávaní

3. **Vylepšenie UI**:
   - Reimplementácia náhľadu obrázkov
   - Pridanie pokročilých filtrov pre výsledky
   - Vylepšenie používateľskej skúsenosti
   - Pridanie indikátorov priebehu pri komunikácii s API

4. **Rozšírenie testovania**:
   - Vytvorenie testovacích dát (vzorové bloky)
   - Implementácia mock objektov pre Gemini API
   - Implementácia integračných testov
   - Automatizácia testovania