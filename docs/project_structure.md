# Štruktúra projektu BLOCEK

Tento dokument popisuje štruktúru adresárov a súborov projektu BLOCEK, ktorý slúži na automatizáciu procesu extrakcie údajov z pokladničných blokov.

## Hlavná štruktúra adresárov

\\\
BLOCEK/

 src/                         # Zdrojový kód aplikácie
    ui/                      # Užívateľské rozhranie
    core/                    # Hlavná logika aplikácie
    utils/                   # Pomocné funkcie a nástroje

 tests/                       # Testy aplikácie

 docs/                        # Dokumentácia

 resources/                   # Zdroje (šablóny, vzorové dáta, ikony)
    templates/               # XML šablóny
    sample_data/             # Vzorové dáta pre testovanie
    icons/                   # Ikony pre UI

 logs/                        # Adresár pre logy aplikácie
\\\

## Podrobný popis adresárov a súborov

### src/ - Zdrojový kód aplikácie

Tento adresár obsahuje všetok zdrojový kód aplikácie, rozdelený do logických podadresárov.

#### src/ui/ - Užívateľské rozhranie

Obsahuje komponenty užívateľského rozhrania aplikácie.

- **main_window.py**: Implementácia hlavného okna aplikácie, ktoré integruje všetky ostatné komponenty UI.
- **directory_selector.py**: Komponenta pre výber adresára s pokladničnými blokmi.
- **file_list.py**: Komponenta pre zobrazenie a výber súborov na spracovanie.

#### src/core/ - Hlavná logika aplikácie

Obsahuje implementáciu hlavnej logiky aplikácie.

- **gemini_api.py**: Integrácia s AI modelom Gemini pre extrakciu údajov z pokladničných blokov.
- **receipt_processor.py**: Spracovanie pokladničných blokov a extrakcia údajov.
- **excel_handler.py**: Práca s Excel súbormi - ukladanie a načítavanie údajov.
- **xml_generator.py**: Generovanie XML súborov na základe šablóny a extrahovaných údajov.

#### src/utils/ - Pomocné funkcie a nástroje

Obsahuje pomocné funkcie a nástroje používané v aplikácii.

- **file_utils.py**: Pomocné funkcie pre prácu so súbormi (napr. validácia cesty, filtrovanie súborov).
- **image_utils.py**: Pomocné funkcie pre prácu s obrázkami (napr. konverzia formátov, úprava veľkosti).
- **security.py**: Bezpečnostné funkcie (napr. bezpečné ukladanie a načítavanie API kľúčov).

### tests/ - Testy aplikácie

Obsahuje testy pre jednotlivé komponenty aplikácie.

- **test_gemini_api.py**: Testy pre integráciu s Gemini API.
- **test_receipt_processor.py**: Testy pre spracovanie pokladničných blokov.
- **test_excel_handler.py**: Testy pre prácu s Excel súbormi.
- **test_xml_generator.py**: Testy pre generovanie XML súborov.

### docs/ - Dokumentácia

Obsahuje dokumentáciu projektu.

- **project_structure.md**: Tento dokument - popis štruktúry projektu.
- **user_guide.md**: Užívateľská príručka s popisom používania aplikácie.
- **developer_guide.md**: Vývojárska dokumentácia s popisom architektúry a implementácie.
- **api_documentation.md**: Dokumentácia API používaných v aplikácii.

### resources/ - Zdroje

Obsahuje rôzne zdroje používané v aplikácii.

#### resources/templates/ - XML šablóny

Obsahuje XML šablóny používané pri generovaní XML súborov.

- **xml_template.xml**: Základná XML šablóna pre generovanie XML súborov.

#### resources/sample_data/ - Vzorové dáta pre testovanie

Obsahuje vzorové dáta používané pri testovaní aplikácie.

- **receipts/**: Vzorové pokladničné bloky v rôznych formátoch (JPG, PNG, PDF).
- **excel/**: Vzorové Excel súbory s údajmi z pokladničných blokov.

#### resources/icons/ - Ikony pre UI

Obsahuje ikony používané v užívateľskom rozhraní aplikácie.

### logs/ - Adresár pre logy aplikácie

Obsahuje logy aplikácie generované počas jej behu.

## Hlavné súbory v koreňovom adresári

- **main.py**: Hlavný vstupný bod aplikácie.
- **config.py**: Konfiguračné nastavenia aplikácie (napr. cesty k súborom, API kľúče).
- **requirements.txt**: Zoznam závislostí projektu pre inštaláciu pomocou pip.
- **setup.py**: Inštalačný skript pre vytvorenie balíčka Python.
- **README.md**: Základné informácie o projekte, inštalácia a použitie.
- **.gitignore**: Zoznam súborov a adresárov, ktoré sa nemajú sledovať v git repozitári.

## Workflow aplikácie

1. Používateľ spustí aplikáciu (main.py).
2. Zobrazí sa hlavné okno aplikácie (main_window.py).
3. Používateľ vyberie adresár s pokladničnými blokmi (directory_selector.py).
4. Aplikácia zobrazí zoznam súborov v adresári (file_list.py).
5. Používateľ vyberie súbory na spracovanie.
6. Aplikácia spracuje vybrané súbory (receipt_processor.py) pomocou AI modelu Gemini (gemini_api.py).
7. Extrahované údaje sa uložia do Excel súboru (excel_handler.py).
8. Používateľ môže generovať XML súbory na základe údajov v Excel súbore (xml_generator.py).

