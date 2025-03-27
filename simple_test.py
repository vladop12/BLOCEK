#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import tkinter as tk

# Pridanie koreňového adresára do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Pokus o import
try:
    print("Pokúšam sa importovať DirectorySelector...")
    from src.ui.directory_selector import DirectorySelector
    print("Import úspešný!")
    
    # Vytvorenie a zobrazenie komponenty
    root = tk.Tk()
    root.title("Test DirectorySelector")
    
    def on_dir_selected(directory):
        print(f"Vybraný adresár: {directory}")
    
    ds = DirectorySelector(root, callback=on_dir_selected)
    ds.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    root.mainloop()
except Exception as e:
    print(f"Chyba pri importe: {e}")
    
    # Výpis dostupných modulov v src.ui
    try:
        import src.ui
        print(f"Dostupné moduly v src.ui: {dir(src.ui)}")
    except Exception as e2:
        print(f"Chyba pri importe src.ui: {e2}")
