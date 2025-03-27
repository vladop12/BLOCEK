#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testovací skript pre komponentu ProcessingPanel.
"""

import tkinter as tk
from tkinter import ttk
import sys
import os
import time
import threading
import logging

# Nastavenie loggeru
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Pridanie koreňového adresára projektu do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ui.processing_panel import ProcessingPanel

class TestProcessingPanel:
    def __init__(self, root):
        self.root = root
        
        # Frame pre komponenty
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Vytvorenie a umiestnenie komponenty ProcessingPanel
        self.processing_panel = ProcessingPanel(
            main_frame, 
            process_callback=self.on_process, 
            generate_xml_callback=self.on_generate_xml
        )
        self.processing_panel.pack(fill=tk.X, padx=5, pady=5)
        
        # Frame pre ovládacie prvky
        control_frame = ttk.Frame(root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Tlačidlo na simuláciu úspešného spracovania
        success_button = ttk.Button(control_frame, text="Simulovať úspešné spracovanie", command=self.simulate_success)
        success_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na simuláciu chyby
        error_button = ttk.Button(control_frame, text="Simulovať chybu", command=self.simulate_error)
        error_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na reset
        reset_button = ttk.Button(control_frame, text="Reset", command=self.reset)
        reset_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo na ukončenie testu
        finish_button = ttk.Button(control_frame, text="Ukončiť test", command=self.finish_test)
        finish_button.pack(side=tk.RIGHT, padx=5)
        
        # Výpis inštrukcií
        print("Test ProcessingPanel:")
        print("1. Kliknite na 'Spracovať vybrané súbory' pre simuláciu spracovania")
        print("2. Kliknite na 'Simulovať úspešné spracovanie' pre simuláciu úspešného spracovania")
        print("3. Kliknite na 'Simulovať chybu' pre simuláciu chyby")
        print("4. Kliknite na 'Reset' pre reset komponenty")
        print("5. Kliknite na 'Ukončiť test'")

    def on_process(self):
        """Callback funkcia volaná po kliknutí na tlačidlo "Spracovať"."""
        print("Spracovanie súborov...")
        self.processing_panel.update_status("Spracovávam súbory...")
        self.processing_panel.enable_buttons(False)
        
        # Simulácia spracovania v samostatnom vlákne
        threading.Thread(target=self.simulate_processing).start()

    def on_generate_xml(self):
        """Callback funkcia volaná po kliknutí na tlačidlo "Generovať XML"."""
        print("Generovanie XML...")
        self.processing_panel.update_status("Generujem XML...")
        self.processing_panel.enable_buttons(False)
        self.processing_panel.enable_xml_button(False)
        
        # Simulácia generovania XML v samostatnom vlákne
        threading.Thread(target=self.simulate_xml_generation).start()

    def simulate_processing(self):
        """Simulácia spracovania súborov."""
        total_files = 10
        
        for i in range(total_files + 1):
            # Simulácia spracovania jedného súboru
            time.sleep(0.2)
            
            # Aktualizácia progress baru a stavu
            self.root.after(0, self.processing_panel.update_progress, i, total_files)
            self.root.after(0, self.processing_panel.update_status, f"Spracovávam súbor {i}/{total_files}")
        
        # Dokončenie spracovania
        self.root.after(0, self.processing_panel.update_status, "Spracovanie dokončené")
        self.root.after(0, self.processing_panel.enable_buttons, True)
        self.root.after(0, self.processing_panel.enable_xml_button, True)

    def simulate_xml_generation(self):
        """Simulácia generovania XML."""
        total_steps = 5
        
        for i in range(total_steps + 1):
            # Simulácia jedného kroku generovania
            time.sleep(0.3)
            
            # Aktualizácia progress baru a stavu
            self.root.after(0, self.processing_panel.update_progress, i, total_steps)
            self.root.after(0, self.processing_panel.update_status, f"Generujem XML {i}/{total_steps}")
        
        # Dokončenie generovania
        self.root.after(0, self.processing_panel.update_status, "Generovanie XML dokončené")
        self.root.after(0, self.processing_panel.enable_buttons, True)
        self.root.after(0, self.processing_panel.enable_xml_button, True)

    def simulate_success(self):
        """Simulácia úspešného spracovania."""
        self.processing_panel.update_status("Spracovanie úspešne dokončené")
        self.processing_panel.update_progress(100, 100)
        self.processing_panel.enable_buttons(True)
        self.processing_panel.enable_xml_button(True)

    def simulate_error(self):
        """Simulácia chyby pri spracovaní."""
        self.processing_panel.update_status("Chyba pri spracovaní: Neplatný formát súboru")
        self.processing_panel.update_progress(0, 100)
        self.processing_panel.enable_buttons(True)
        self.processing_panel.enable_xml_button(False)

    def reset(self):
        """Reset komponenty."""
        self.processing_panel.reset()

    def finish_test(self):
        """Ukončenie testu."""
        print("Test komponenty ProcessingPanel ukončený")
        self.root.destroy()

def main():
    """Hlavná funkcia testovacieho skriptu."""
    # Vytvorenie hlavného okna
    root = tk.Tk()
    root.title("Test ProcessingPanel")
    root.geometry("600x250")
    
    # Spustenie testu
    test = TestProcessingPanel(root)
    
    # Spustenie hlavnej slučky
    root.mainloop()

if __name__ == "__main__":
    main()
