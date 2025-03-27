#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MainWindow - Hlavné okno aplikácie pre spracovanie pokladničných blokov.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import logging
import os
import sys
import threading
import time
import tempfile

# Pridanie koreňového adresára projektu do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ui.directory_selector import DirectorySelector
#from src.ui.image_preview import ImagePreview
from src.ui.file_list import FileList
from src.ui.processing_options import ProcessingOptions
from src.ui.processing_panel import ProcessingPanel
from src.ui.results_viewer import ResultsViewer

# Nastavenie loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class MainWindow:
    """
    Hlavné okno aplikácie pre spracovanie pokladničných blokov.
    """
    
    def __init__(self, root):
        """
        Inicializácia hlavného okna aplikácie.
        
        Args:
            root: Koreňový widget Tkinter
        """
        self.root = root
        self.root.title("Spracovanie pokladničných blokov")
        self.root.geometry("1200x800")
        
        # Nastavenie štýlu
        self.setup_style()
        
        # Vytvorenie hlavného menu
        self.create_menu()
        
        # Vytvorenie hlavného rozloženia
        self.create_layout()
        
        # Nastavenie callbackov
        self.setup_callbacks()
        
        logger.info("Hlavné okno aplikácie inicializované")
    
    def setup_style(self):
        """Nastavenie štýlu aplikácie."""
        style = ttk.Style()
        
        # Nastavenie témy
        if "clam" in style.theme_names():
            style.theme_use("clam")
        
        # Nastavenie štýlov pre jednotlivé widgety
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10))
        style.configure("TNotebook", background="#f0f0f0")
        style.configure("TNotebook.Tab", font=("Arial", 10))
    def create_menu(self):
        """Vytvorenie hlavného menu aplikácie."""
        # Vytvorenie menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        # Menu Súbor
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Otvoriť súbory", command=self.on_open_files)
        file_menu.add_command(label="Uložiť výsledky", command=self.on_save_results)
        file_menu.add_separator()
        file_menu.add_command(label="Ukončiť", command=self.on_exit)
        self.menu.add_cascade(label="Súbor", menu=file_menu)
        
        # Menu Spracovanie
        process_menu = tk.Menu(self.menu, tearoff=0)
        process_menu.add_command(label="Spracovať vybrané súbory", command=self.on_process_files)
        process_menu.add_command(label="Generovať XML", command=self.on_generate_xml)
        self.menu.add_cascade(label="Spracovanie", menu=process_menu)
        
        # Menu Pomoc
        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Návod", command=self.on_help)
        help_menu.add_command(label="O aplikácii", command=self.on_about)
        self.menu.add_cascade(label="Pomoc", menu=help_menu)
    
    def create_layout(self):
        """Vytvorenie hlavného rozloženia aplikácie."""
        # Hlavný frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Horný frame pre výber súborov a náhľad
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Ľavý frame pre výber súborov a zoznam súborov
        left_frame = ttk.Frame(top_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Frame pre výber súborov
        file_selector_frame = ttk.LabelFrame(left_frame, text="Výber súborov")
        file_selector_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Komponenta pre výber súborov
        self.file_selector = DirectorySelector(file_selector_frame)
        self.file_selector.pack(fill=tk.X, padx=5, pady=5)
        
        # Frame pre zoznam súborov
        file_list_frame = ttk.LabelFrame(left_frame, text="Zoznam vybraných súborov")
        file_list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Komponenta pre zoznam súborov
        self.file_list = FileList(file_list_frame)
        self.file_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Pravý frame pre náhľad obrázka
        right_frame = ttk.Frame(top_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Frame pre náhľad (bez funkčnosti náhľadu obrázka)
        preview_frame = ttk.LabelFrame(right_frame, text="Náhľad")
        preview_frame.pack(fill=tk.BOTH, expand=True)

        # Jednoduchý placeholder namiesto náhľadu obrázka
        placeholder_label = ttk.Label(preview_frame, text="Náhľad nie je k dispozícii")
        placeholder_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Stredný frame pre možnosti spracovania a panel spracovania
        middle_frame = ttk.Frame(main_frame)
        middle_frame.pack(fill=tk.X, pady=5)
        
        # Frame pre možnosti spracovania
        options_frame = ttk.LabelFrame(middle_frame, text="Možnosti spracovania")
        options_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Komponenta pre možnosti spracovania
        self.processing_options = ProcessingOptions(options_frame)
        self.processing_options.pack(fill=tk.X, padx=5, pady=5)
        
        # Frame pre panel spracovania
        processing_frame = ttk.LabelFrame(middle_frame, text="Spracovanie")
        processing_frame.pack(fill=tk.X)
        
        # Komponenta pre panel spracovania
        self.processing_panel = ProcessingPanel(
            processing_frame,
            process_callback=self.on_process_files,
            generate_xml_callback=self.on_generate_xml
        )
        self.processing_panel.pack(fill=tk.X, padx=5, pady=5)
        
        # Dolný frame pre výsledky
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Frame pre výsledky
        results_frame = ttk.LabelFrame(bottom_frame, text="Výsledky spracovania")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Komponenta pre zobrazenie výsledkov
        self.results_viewer = ResultsViewer(results_frame)
        self.results_viewer.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    def setup_callbacks(self):
        """Nastavenie callbackov medzi komponentami."""
        # Prepojenie DirectorySelector a FileList
        self.file_selector.callback = self.on_files_selected  # Zmenené z set_directory_selected_callback


    
    def on_files_selected(self, file_paths):
        """
        Callback volaný po výbere súborov.
    
        Args:
            file_paths: Zoznam ciest k vybraným súborom
        """
        logger.info(f"Vybrané súbory: {file_paths}")
        self.file_list.update_file_list(file_paths)
    
        # Odstránené volanie select_first_file
        # if file_paths:
        #     self.file_list.select_first_file()

    
    def on_file_list_selection(self, file_path):
        """
        Callback volaný po výbere súboru v zozname.
    
        Args:
          file_path: Cesta k vybranému súboru
        """
        logger.info(f"Vybraný súbor v zozname: {file_path}")
        # Odstránené volanie self.image_preview.load_image(file_path)

    def on_process_files(self):
        """Callback volaný po kliknutí na tlačidlo 'Spracovať vybrané súbory'."""
        logger.info("Spracovanie vybraných súborov")
        
        # Získanie vybraných súborov
        selected_files = self.file_list.get_file_list()
        if not selected_files:
            logger.warning("Nie sú vybrané žiadne súbory na spracovanie")
            return
        
        # Získanie možností spracovania
        options = self.processing_options.get_options()
        logger.info(f"Možnosti spracovania: {options}")
        
        # Simulácia spracovania
        self.processing_panel.update_status("Spracovávam súbory...")
        self.processing_panel.enable_buttons(False)
        
        # Tu by bola skutočná logika spracovania
        # Pre účely demonštrácie len simulujeme spracovanie
        
        def simulate_processing():
            total_files = len(selected_files)
            
            for i, file_path in enumerate(selected_files):
                # Simulácia spracovania jedného súboru
                time.sleep(0.5)
                
                # Aktualizácia progress baru a stavu
                self.root.after(0, self.processing_panel.update_progress, i + 1, total_files)
                self.root.after(0, self.processing_panel.update_status, f"Spracovávam súbor {i + 1}/{total_files}: {os.path.basename(file_path)}")
            
            # Vytvorenie vzorových výsledkov
            sample_results = []
            for i, file_path in enumerate(selected_files):
                sample_results.append({
                    "file": os.path.basename(file_path),
                    "date": f"2023-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
                    "total": f"{(i + 1) * 10.5:.2f} €",
                    "store": ["Tesco", "Lidl", "Kaufland", "Billa"][i % 4]
                })
            
            # Aktualizácia výsledkov
            self.root.after(0, self.results_viewer.update_results, sample_results)
            
            # Dokončenie spracovania
            self.root.after(0, self.processing_panel.update_status, "Spracovanie dokončené")
            self.root.after(0, self.processing_panel.enable_buttons, True)
            self.root.after(0, self.processing_panel.enable_xml_button, True)
        
        # Spustenie simulácie v samostatnom vlákne
        threading.Thread(target=simulate_processing).start()
    def on_generate_xml(self):
        """Callback volaný po kliknutí na tlačidlo 'Generovať XML'."""
        logger.info("Generovanie XML")
        
        # Simulácia generovania XML
        self.processing_panel.update_status("Generujem XML...")
        self.processing_panel.enable_buttons(False)
        self.processing_panel.enable_xml_button(False)
        
        # Tu by bola skutočná logika generovania XML
        # Pre účely demonštrácie len simulujeme generovanie
        
        def simulate_xml_generation():
            total_steps = 3
            
            for i in range(total_steps):
                # Simulácia jedného kroku generovania
                time.sleep(0.7)
                
                # Aktualizácia progress baru a stavu
                self.root.after(0, self.processing_panel.update_progress, i + 1, total_steps)
                self.root.after(0, self.processing_panel.update_status, f"Generujem XML {i + 1}/{total_steps}")
            
            # Vytvorenie vzorového Excel súboru
            with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
                excel_path = temp_file.name
            
            # Aktualizácia výsledkov s cestou k Excel súboru
            self.root.after(0, self.results_viewer.update_results, self.results_viewer.results, excel_path)
            
            # Dokončenie generovania
            self.root.after(0, self.processing_panel.update_status, "Generovanie XML dokončené")
            self.root.after(0, self.processing_panel.enable_buttons, True)
            self.root.after(0, self.processing_panel.enable_xml_button, True)
        
        # Spustenie simulácie v samostatnom vlákne
        threading.Thread(target=simulate_xml_generation).start()
    
    def on_open_files(self):
        """Callback volaný po výbere položky menu 'Otvoriť súbory'."""
        logger.info("Otvorenie súborov cez menu")
        self.file_selector.browse_directory()  # Zmenené z select_files na browse_directory

    
    def on_save_results(self):
        """Callback volaný po výbere položky menu 'Uložiť výsledky'."""
        logger.info("Uloženie výsledkov")
        
        # Kontrola, či existujú výsledky na uloženie
        if not self.results_viewer.results:
            messagebox.showwarning("Upozornenie", "Nie sú k dispozícii žiadne výsledky na uloženie.")
            return
        
        # Výber cieľového súboru
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel súbory", "*.xlsx"), ("Všetky súbory", "*.*")],
            title="Uložiť výsledky ako"
        )
        
        if not file_path:
            logger.info("Uloženie výsledkov zrušené")
            return
        
        # Tu by bola skutočná logika uloženia výsledkov
        # Pre účely demonštrácie len simulujeme uloženie
        try:
            # Vytvorenie prázdneho súboru
            with open(file_path, 'w') as f:
                f.write("# Simulácia uloženia výsledkov\n")
            
            messagebox.showinfo("Informácia", f"Výsledky boli úspešne uložené do súboru:\n{file_path}")
            logger.info(f"Výsledky uložené do súboru: {file_path}")
        except Exception as e:
            messagebox.showerror("Chyba", f"Nepodarilo sa uložiť výsledky: {e}")
            logger.error(f"Chyba pri ukladaní výsledkov: {e}")
    
    def on_exit(self):
        """Callback volaný po výbere položky menu 'Ukončiť'."""
        logger.info("Ukončenie aplikácie")
        self.root.destroy()
    
    def on_help(self):
        """Callback volaný po výbere položky menu 'Návod'."""
        logger.info("Zobrazenie návodu")
        messagebox.showinfo(
            "Návod",
            "Návod na použitie aplikácie:\n\n"
            "1. Vyberte súbory na spracovanie pomocou tlačidla 'Vybrať súbory'\n"
            "2. Nastavte možnosti spracovania\n"
            "3. Kliknite na tlačidlo 'Spracovať vybrané súbory'\n"
            "4. Po dokončení spracovania môžete generovať XML pomocou tlačidla 'Generovať XML'\n"
            "5. Výsledky môžete uložiť pomocou menu 'Súbor' > 'Uložiť výsledky'"
        )
    
    def on_about(self):
        """Callback volaný po výbere položky menu 'O aplikácii'."""
        logger.info("Zobrazenie informácií o aplikácii")
        messagebox.showinfo(
            "O aplikácii",
            "Aplikácia na spracovanie pokladničných blokov\n\n"
            "Verzia: 1.0.0\n"
            "Autor: Váš tím\n\n"
            "© 2023 Všetky práva vyhradené"
        )
def main():
    """Hlavná funkcia aplikácie."""
    # Vytvorenie hlavného okna
    root = tk.Tk()
    
    # Vytvorenie inštancie hlavného okna aplikácie
    app = MainWindow(root)
    
    # Spustenie hlavnej slučky
    root.mainloop()

if __name__ == "__main__":
    main()
