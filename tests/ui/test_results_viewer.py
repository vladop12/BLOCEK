#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testovací skript pre komponentu ResultsViewer.
"""

import tkinter as tk
from tkinter import ttk
import sys
import os
import logging
import tempfile

# Nastavenie loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Pridanie koreňového adresára projektu do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ui.results_viewer import ResultsViewer

class TestResultsViewer:
    def __init__(self, root):
        self.root = root
        
        # Frame pre komponenty
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Vytvorenie a umiestnenie komponenty ResultsViewer
        self.results_viewer = ResultsViewer(main_frame)
        self.results_viewer.pack(fill=tk.BOTH, expand=True)
        
        # Frame pre ovládacie prvky
        control_frame = ttk.Frame(root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Tlačidlo na zobrazenie vzorových výsledkov
        show_results_button = ttk.Button(control_frame, text="Zobraziť vzorové výsledky", command=self.show_sample_results)
        show_results_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na vyčistenie výsledkov
        clear_button = ttk.Button(control_frame, text="Vyčistiť výsledky", command=self.clear_results)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na vytvorenie vzorového Excel súboru
        create_excel_button = ttk.Button(control_frame, text="Vytvoriť vzorový Excel", command=self.create_sample_excel)
        create_excel_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na ukončenie testu
        finish_button = ttk.Button(control_frame, text="Ukončiť test", command=self.finish_test)
        finish_button.pack(side=tk.RIGHT, padx=5)
        
        # Výpis inštrukcií
        print("Test ResultsViewer:")
        print("1. Kliknite na 'Zobraziť vzorové výsledky' pre zobrazenie vzorových údajov")
        print("2. Kliknite na 'Vyčistiť výsledky' pre vyčistenie zobrazených údajov")
        print("3. Kliknite na 'Vytvoriť vzorový Excel' pre vytvorenie vzorového súboru")
        print("4. Kliknite na 'Ukončiť test'")

    def show_sample_results(self):
        """Zobrazenie vzorových výsledkov."""
        # Vzorové výsledky
        sample_results = [
            {"file": "blocek_1.jpg", "date": "2023-01-15", "total": "25.99 €", "store": "Tesco"},
            {"file": "blocek_2.jpg", "date": "2023-01-20", "total": "12.50 €", "store": "Lidl"},
            {"file": "blocek_3.jpg", "date": "2023-02-05", "total": "45.30 €", "store": "Kaufland"},
            {"file": "blocek_4.jpg", "date": "2023-02-10", "total": "8.75 €", "store": "Billa"},
            {"file": "blocek_5.jpg", "date": "2023-03-01", "total": "32.15 €", "store": "Tesco"},
            {"file": "blocek_6.jpg", "date": "2023-03-15", "total": "18.90 €", "store": "Lidl"},
            {"file": "blocek_7.jpg", "date": "2023-04-02", "total": "55.60 €", "store": "Kaufland"},
            {"file": "blocek_8.jpg", "date": "2023-04-10", "total": "15.25 €", "store": "Billa"},
            {"file": "blocek_9.jpg", "date": "2023-05-05", "total": "28.70 €", "store": "Tesco"},
            {"file": "blocek_10.jpg", "date": "2023-05-20", "total": "42.35 €", "store": "Lidl"}
        ]
        
        # Aktualizácia výsledkov bez Excel súboru
        self.results_viewer.update_results(sample_results)
        print("Vzorové výsledky zobrazené")

    def clear_results(self):
        """Vyčistenie výsledkov."""
        self.results_viewer.clear()
        print("Výsledky vyčistené")

    def create_sample_excel(self):
        """Vytvorenie vzorového Excel súboru."""
        try:
            # Vytvorenie dočasného súboru
            with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
                excel_path = temp_file.name
            
            # Vzorové výsledky
            sample_results = [
                {"file": "blocek_1.jpg", "date": "2023-01-15", "total": "25.99 €", "store": "Tesco"},
                {"file": "blocek_2.jpg", "date": "2023-01-20", "total": "12.50 €", "store": "Lidl"},
                {"file": "blocek_3.jpg", "date": "2023-02-05", "total": "45.30 €", "store": "Kaufland"},
                {"file": "blocek_4.jpg", "date": "2023-02-10", "total": "8.75 €", "store": "Billa"},
                {"file": "blocek_5.jpg", "date": "2023-03-01", "total": "32.15 €", "store": "Tesco"}
            ]
            
            # Vytvorenie jednoduchého textového súboru namiesto Excel súboru
            # Použitie UTF-8 kódovania pre podporu slovenských znakov
            with open(excel_path, 'w', encoding='utf-8') as f:
                f.write("Toto je vzorovy subor namiesto Excel suboru\n")
                f.write("V realnej aplikacii by tu bol skutocny Excel subor\n\n")
                
                f.write("Subor,Datum,Celkova suma,Obchod\n")
                for result in sample_results:
                    f.write(f"{result['file']},{result['date']},{result['total']},{result['store']}\n")
            
            # Aktualizácia výsledkov s cestou k Excel súboru
            self.results_viewer.update_results(sample_results, excel_path)
            print(f"Vzorový súbor vytvorený: {excel_path}")
            
        except Exception as e:
            print(f"Chyba pri vytváraní vzorového súboru: {e}")

    def finish_test(self):
        """Ukončenie testu."""
        print("Test komponenty ResultsViewer ukončený")
        self.root.destroy()

def main():
    """Hlavná funkcia testovacieho skriptu."""
    # Vytvorenie hlavného okna
    root = tk.Tk()
    root.title("Test ResultsViewer")
    root.geometry("800x600")
    
    # Spustenie testu
    test = TestResultsViewer(root)
    
    # Spustenie hlavnej slučky
    root.mainloop()

if __name__ == "__main__":
    main()
