#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testovací skript pre komponentu FileList.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
import logging

# Nastavenie loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Pridanie koreňového adresára projektu do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ui.file_list import FileList

class TestFileList:
    def __init__(self, root):
        self.root = root
        
        # Frame pre komponenty
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Vytvorenie a umiestnenie komponenty FileList
        self.file_list = FileList(main_frame)
        self.file_list.pack(fill=tk.BOTH, expand=True)
        
        # Frame pre ovládacie prvky
        control_frame = ttk.Frame(root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Entry pre zadanie cesty k adresáru
        ttk.Label(control_frame, text="Adresár:").grid(row=0, column=0, padx=5, pady=5)
        self.dir_var = tk.StringVar(value=os.path.expanduser("~"))
        dir_entry = ttk.Entry(control_frame, textvariable=self.dir_var, width=50)
        dir_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Tlačidlo na aktualizáciu zoznamu súborov
        update_button = ttk.Button(control_frame, text="Aktualizovať zoznam", command=self.update_file_list)
        update_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Tlačidlo na zobrazenie vybraných súborov
        show_selected_button = ttk.Button(control_frame, text="Zobraziť vybrané súbory", command=self.show_selected_files)
        show_selected_button.grid(row=1, column=1, padx=5, pady=5)
        
        # Tlačidlo na ukončenie testu
        finish_button = ttk.Button(control_frame, text="Ukončiť test", command=self.finish_test)
        finish_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Nastavenie roztiahnutia stĺpcov
        control_frame.columnconfigure(1, weight=1)
        
        # Výpis inštrukcií
        print("Test FileList:")
        print("1. Zadajte cestu k adresáru alebo použite predvolenú cestu")
        print("2. Kliknite na 'Aktualizovať zoznam' pre zobrazenie súborov")
        print("3. Vyberte súbory v zozname")
        print("4. Kliknite na 'Zobraziť vybrané súbory' pre výpis vybraných súborov")
        print("5. Vyskúšajte checkbox 'Vybrať všetky'")
        print("6. Kliknite na 'Ukončiť test'")

    def update_file_list(self):
        """Aktualizácia zoznamu súborov."""
        directory = self.dir_var.get()
        print(f"Aktualizujem zoznam súborov z adresára: {directory}")
        self.file_list.update_file_list(directory)

    def show_selected_files(self):
        """Zobrazenie vybraných súborov."""
        selected_files = self.file_list.get_selected_files()
        if selected_files:
            print(f"Vybrané súbory ({len(selected_files)}):")
            for file in selected_files:
                print(f"- {file}")
        else:
            print("Nie sú vybrané žiadne súbory")
            messagebox.showinfo("Žiadne súbory", "Nie sú vybrané žiadne súbory")

    def finish_test(self):
        """Ukončenie testu."""
        print("Test komponenty FileList ukončený")
        self.root.destroy()

def main():
    """Hlavná funkcia testovacieho skriptu."""
    # Vytvorenie hlavného okna
    root = tk.Tk()
    root.title("Test FileList")
    root.geometry("800x600")
    
    # Spustenie testu
    test = TestFileList(root)
    
    # Spustenie hlavnej slučky
    root.mainloop()

if __name__ == "__main__":
    main()
