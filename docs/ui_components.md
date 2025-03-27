# Dokumentácia UI komponentov projektu BLOCEK

Tento dokument popisuje UI komponenty aplikácie BLOCEK, ich účel, funkcionalitu a vzájomné interakcie.

## Prehľad UI komponentov

Aplikácia BLOCEK pozostáva z nasledujúcich UI komponentov:

1. **MainWindow** - Hlavné okno aplikácie
2. **DirectorySelector** - Komponenta pre výber adresára
3. **FileList** - Komponenta pre zobrazenie a výber súborov
4. **ProcessingOptions** - Komponenta pre nastavenie možností spracovania
5. **ProcessingPanel** - Komponenta pre spracovanie vybraných súborov
6. **ResultsViewer** - Komponenta pre zobrazenie výsledkov spracovania

## Detailný popis komponentov

### 1. MainWindow (src/ui/main_window.py)

**Účel:** Hlavné okno aplikácie, ktoré integruje všetky ostatné komponenty a poskytuje základný rámec aplikácie.

**Funkcionalita:**
- Inicializácia a rozloženie všetkých UI komponentov
- Správa hlavného menu aplikácie
- Správa stavového riadku
- Koordinácia interakcií medzi komponentami

**Rozloženie:**
- V hornej časti okna sa nachádza DirectorySelector
- Pod ním je umiestnený FileList
- V strednej časti sa nachádza ProcessingOptions
- V spodnej časti okna sa nachádza ProcessingPanel
- Po spracovaní súborov sa zobrazí ResultsViewer

**Metódy:**
- __init__(self, root) - Inicializácia hlavného okna
- setup_ui(self) - Nastavenie užívateľského rozhrania
- setup_menu(self) - Nastavenie hlavného menu
- on_directory_selected(self, directory) - Callback metóda volaná po výbere adresára
- on_process_files(self) - Callback metóda volaná po kliknutí na tlačidlo "Spracovať"
- on_generate_xml(self) - Callback metóda volaná po kliknutí na tlačidlo "Generovať XML"
- show_about_dialog(self) - Zobrazenie dialógu "O aplikácii"
- show_help(self) - Zobrazenie pomocníka
- exit_application(self) - Ukončenie aplikácie

### 2. DirectorySelector (src/ui/directory_selector.py)

**Účel:** Komponenta pre výber adresára s pokladničnými blokmi.

**Funkcionalita:**
- Zobrazenie aktuálne vybraného adresára
- Tlačidlo pre otvorenie dialógu na výber adresára
- Notifikácia MainWindow o zmene vybraného adresára

**Rozloženie:**
- Label s textom "Vyberte adresár s pokladničnými blokmi:"
- Entry pole zobrazujúce cestu k vybranému adresáru
- Tlačidlo "Prehľadávať..." pre otvorenie dialógu na výber adresára

**Metódy:**
- __init__(self, parent, callback=None) - Inicializácia komponenty
- setup_ui(self) - Nastavenie užívateľského rozhrania
- rowse_directory(self) - Otvorenie dialógu na výber adresára
- get_directory(self) - Získanie aktuálne vybraného adresára

### 3. FileList (src/ui/file_list.py)

**Účel:** Komponenta pre zobrazenie a výber súborov na spracovanie.

**Funkcionalita:**
- Zobrazenie zoznamu súborov v vybranom adresári
- Možnosť výberu súborov na spracovanie
- Filtrovanie súborov podľa podporovaných formátov

**Rozloženie:**
- Label s textom "Zoznam súborov:"
- Treeview so stĺpcami "Názov súboru", "Typ" a "Veľkosť"
- Scrollbar pre Treeview
- Checkbox "Vybrať všetky" pre výber všetkých súborov

**Metódy:**
- __init__(self, parent) - Inicializácia komponenty
- setup_ui(self) - Nastavenie užívateľského rozhrania
- update_file_list(self, directory) - Aktualizácia zoznamu súborov podľa vybraného adresára
- get_selected_files(self) - Získanie zoznamu vybraných súborov
- 	oggle_select_all(self) - Prepínanie výberu všetkých súborov

### 4. ProcessingOptions (src/ui/processing_options.py)

**Účel:** Komponenta pre nastavenie možností spracovania pokladničných blokov.

**Funkcionalita:**
- Nastavenie formátu výstupu (CSV, Excel, JSON)
- Nastavenie zoskupenia výsledkov (žiadne, podľa dátumu, podľa obchodu)
- Nastavenie ďalších možností (zahrnúť DPH, kategorizovať položky)
- Filtrovanie podľa dátumu

**Rozloženie:**
- Frame s možnosťami formátu výstupu (CSV, Excel, JSON)
- Frame s možnosťami zoskupenia výsledkov
- Frame s ďalšími možnosťami (checkboxy)
- Frame s nastavením filtrovania podľa dátumu

**Metódy:**
- __init__(self, parent, callback=None) - Inicializácia komponenty
- setup_ui(self) - Nastavenie užívateľského rozhrania
- _on_settings_changed(self) - Callback metóda volaná po zmene nastavení
- _on_date_range_changed(self) - Callback metóda volaná po zmene nastavenia filtrovania podľa dátumu
- get_options(self) - Získanie aktuálnych nastavení spracovania

### 5. ProcessingPanel (src/ui/processing_panel.py)

**Účel:** Komponenta pre spracovanie vybraných súborov a zobrazenie stavu spracovania.

**Funkcionalita:**
- Tlačidlá pre spracovanie súborov a generovanie XML
- Zobrazenie progress baru počas spracovania
- Zobrazenie stavu spracovania

**Rozloženie:**
- Frame s tlačidlami "Spracovať vybrané súbory" a "Generovať XML"
- Progress bar zobrazujúci priebeh spracovania
- Label zobrazujúci stav spracovania

**Metódy:**
- __init__(self, parent, process_callback=None, generate_xml_callback=None) - Inicializácia komponenty
- setup_ui(self) - Nastavenie užívateľského rozhrania
- on_process_button_click(self) - Callback metóda volaná po kliknutí na tlačidlo "Spracovať"
- on_generate_xml_button_click(self) - Callback metóda volaná po kliknutí na tlačidlo "Generovať XML"
- update_progress(self, value, max_value) - Aktualizácia progress baru
- update_status(self, status) - Aktualizácia stavu spracovania
- enable_buttons(self, enable) - Povolenie/zakázanie tlačidiel počas spracovania

### 6. ResultsViewer (src/ui/results_viewer.py)

**Účel:** Komponenta pre zobrazenie výsledkov spracovania.

**Funkcionalita:**
- Zobrazenie extrahovaných údajov z pokladničných blokov
- Možnosť úpravy extrahovaných údajov
- Zobrazenie cesty k vygenerovanému Excel súboru

**Rozloženie:**
- Treeview so stĺpcami "Súbor", "Dátum", "Celková suma", "Obchod"
- Scrollbar pre Treeview
- Label zobrazujúci cestu k vygenerovanému Excel súboru
- Tlačidlo "Otvoriť Excel" pre otvorenie vygenerovaného Excel súboru

**Metódy:**
- __init__(self, parent) - Inicializácia komponenty
- setup_ui(self) - Nastavenie užívateľského rozhrania
- update_results(self, results, excel_path) - Aktualizácia zobrazených výsledkov
- open_excel(self) - Otvorenie vygenerovaného Excel súboru

## Interakcie medzi komponentami

1. **MainWindow** inicializuje všetky ostatné komponenty a nastavuje callbacky.
2. Keď používateľ vyberie adresár pomocou **DirectorySelector**, MainWindow zavolá metódu update_file_list komponenty **FileList**.
3. Používateľ nastaví možnosti spracovania pomocou **ProcessingOptions**.
4. Keď používateľ klikne na tlačidlo "Spracovať" v **ProcessingPanel**, MainWindow získa vybrané súbory z **FileList**, nastavenia z **ProcessingOptions** a spustí ich spracovanie.
5. Počas spracovania MainWindow aktualizuje progress bar a stav v **ProcessingPanel**.
6. Po dokončení spracovania MainWindow zobrazí výsledky v **ResultsViewer**.
7. Keď používateľ klikne na tlačidlo "Generovať XML" v **ProcessingPanel**, MainWindow spustí generovanie XML súborov.

## Workflow používateľa

1. Používateľ spustí aplikáciu a zobrazí sa **MainWindow**.
2. Používateľ vyberie adresár s pokladničnými blokmi pomocou **DirectorySelector**.
3. **FileList** zobrazí zoznam súborov v vybranom adresári.
4. Používateľ vyberie súbory na spracovanie v **FileList**.
5. Používateľ nastaví možnosti spracovania v **ProcessingOptions**.
6. Používateľ klikne na tlačidlo "Spracovať" v **ProcessingPanel**.
7. Aplikácia spracuje vybrané súbory podľa nastavených možností a zobrazí výsledky v **ResultsViewer**.
8. Používateľ môže kliknúť na tlačidlo "Generovať XML" v **ProcessingPanel** pre generovanie XML súborov.
