#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testovací skript pre komponentu ProcessingOptions.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
import json
import logging

# Nastavenie loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Pridanie koreňového adresára projektu do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ui.processing_options import ProcessingOptions

class TestProcessingOptions:
    def __init__(self, root):
        self.root = root
        
        # Frame pre komponenty
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Vytvorenie a umiestnenie komponenty ProcessingOptions
        self.processing_options = ProcessingOptions(main_frame, callback=self.on_options_changed)
        self.processing_options.pack(fill=tk.BOTH, expand=True)
        
        # Frame pre ovládacie prvky
        control_frame = ttk.Frame(root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Tlačidlo na zobrazenie aktuálnych nastavení
        show_options_button = ttk.Button(control_frame, text="Zobraziť aktuálne nastavenia", command=self.show_options)
        show_options_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na ukončenie testu
        finish_button = ttk.Button(control_frame, text="Ukončiť test", command=self.finish_test)
        finish_button.pack(side=tk.RIGHT, padx=5)
        
        # Výpis inštrukcií
        print("Test ProcessingOptions:")
        print("1. Zmeňte rôzne nastavenia v komponente")
        print("2. Kliknite na 'Zobraziť aktuálne nastavenia' pre výpis nastavení")
        print("3. Kliknite na 'Ukončiť test'")

    def on_options_changed(self, options):
        """Callback funkcia volaná po zmene nastavení."""
        print(f"Nastavenia zmenené: {json.dumps(options, indent=2)}")

    def show_options(self):
        """Zobrazenie aktuálnych nastavení."""
        options = self.processing_options.get_options()
        print(f"Aktuálne nastavenia: {json.dumps(options, indent=2)}")
        
        # Zobrazenie nastavení v dialógovom okne
        messagebox.showinfo(
            "Aktuálne nastavenia",
            f"Formát výstupu: {options['output_format']}\n"
            f"Zoskupenie: {options['group_by']}\n"
            f"Zahrnúť DPH: {options['include_tax']}\n"
            f"Kategorizovať: {options['categorize']}\n"
            f"Filtrovanie podľa dátumu: {options['date_range']['enabled']}\n"
            f"Od: {options['date_range']['start_date'] or 'N/A'}\n"
            f"Do: {options['date_range']['end_date'] or 'N/A'}"
        )

    def finish_test(self):
        """Ukončenie testu."""
        print("Test komponenty ProcessingOptions ukončený")
        self.root.destroy()

def main():
    """Hlavná funkcia testovacieho skriptu."""
    # Vytvorenie hlavného okna
    root = tk.Tk()
    root.title("Test ProcessingOptions")
    root.geometry("500x600")
    
    # Spustenie testu
    test = TestProcessingOptions(root)
    
    # Spustenie hlavnej slučky
    root.mainloop()

if __name__ == "__main__":
    main()
