#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testovací skript pre komponentu DirectorySelector.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Pridanie koreňového adresára projektu do PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

try:
    from src.ui.directory_selector import DirectorySelector
    print("Import DirectorySelector úspešný")
except ImportError as e:
    print(f"Chyba pri importe: {e}")
    sys.exit(1)

class TestDirectorySelector:
    def __init__(self, root):
        self.root = root
        self.test_passed = False
        
        # Vytvorenie a umiestnenie komponenty DirectorySelector
        self.directory_selector = DirectorySelector(root, callback=self.on_directory_selected)
        self.directory_selector.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pridanie tlačidla na ukončenie testu
        self.finish_button = ttk.Button(root, text="Ukončiť test", command=self.finish_test)
        self.finish_button.pack(pady=10)
        
        # Výpis inštrukcií
        print("Test DirectorySelector:")
        print("1. Kliknite na tlačidlo 'Prehľadávať...'")
        print("2. Vyberte adresár")
        print("3. Skontrolujte, či sa cesta zobrazila v textovom poli")
        print("4. Skontrolujte, či sa v konzole vypísal vybraný adresár")
        print("5. Kliknite na tlačidlo 'Ukončiť test'")

    def on_directory_selected(self, directory):
        """Callback funkcia volaná po výbere adresára."""
        print(f"Vybraný adresár: {directory}")
        if directory:
            self.test_passed = True
            print("✓ Adresár bol úspešne vybraný")
        else:
            print("✗ Adresár nebol vybraný")

    def finish_test(self):
        """Ukončenie testu a zobrazenie výsledku."""
        if self.test_passed:
            messagebox.showinfo("Test úspešný", "Test komponenty DirectorySelector bol úspešný!")
            print("✓ Test komponenty DirectorySelector bol úspešný")
        else:
            messagebox.showwarning("Test neúspešný", "Test komponenty DirectorySelector nebol úspešný. Nevybrali ste žiadny adresár.")
            print("✗ Test komponenty DirectorySelector nebol úspešný")
        
        self.root.destroy()

def main():
    """Hlavná funkcia testovacieho skriptu."""
    # Vytvorenie hlavného okna
    root = tk.Tk()
    root.title("Test DirectorySelector")
    root.geometry("600x200")
    
    # Spustenie testu
    test = TestDirectorySelector(root)
    
    # Spustenie hlavnej slučky
    root.mainloop()

if __name__ == "__main__":
    main()
