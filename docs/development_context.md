# Vývojový kontext projektu BLOCEK

Tento dokument slúži na udržiavanie kontextu vývoja projektu BLOCEK. Obsahuje aktuálny stav, rozhodnutia a ďalšie kroky.

## Aktuálny stav projektu

- Vytvorená základná adresárová štruktúra projektu
- Vytvorené základné súbory:
  - README.md - základné informácie o projekte
  - config.py - konfiguračné nastavenia
  - main.py - hlavný vstupný bod aplikácie

## Dokončené úlohy

- [x] Vytvorenie dokumentácie štruktúry projektu (docs/project_structure.md)
- [x] Vytvorenie základnej adresárovej štruktúry
- [x] Vytvorenie základných súborov (README.md, config.py, main.py)

## Aktuálne rozpracované úlohy

- [ ] Implementácia UI komponentov
- [ ] Implementácia core funkcionality
- [ ] Implementácia integrácie s Gemini API

## Ďalšie kroky

1. Implementácia UI komponentov:
   - src/ui/main_window.py
   - src/ui/directory_selector.py
   - src/ui/file_list.py

2. Implementácia core funkcionality:
   - src/core/gemini_api.py
   - src/core/receipt_processor.py
   - src/core/excel_handler.py
   - src/core/xml_generator.py

3. Implementácia pomocných funkcií:
   - src/utils/file_utils.py
   - src/utils/image_utils.py
   - src/utils/security.py

## Technické rozhodnutia

- Použitie tkinter pre UI
- Použitie Gemini API pre extrakciu údajov z pokladničných blokov
- Ukladanie údajov do Excel súborov
- Generovanie XML súborov na základe šablóny
