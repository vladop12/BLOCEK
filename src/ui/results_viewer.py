#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ResultsViewer - Komponenta pre zobrazenie výsledkov spracovania pokladničných blokov.
"""

import tkinter as tk
from tkinter import ttk
import logging
import os
import subprocess
import platform

logger = logging.getLogger(__name__)

class ResultsViewer(ttk.Frame):
    """
    Komponenta pre zobrazenie výsledkov spracovania pokladničných blokov.
    
    Atribúty:
        parent: Rodičovský widget
    """
    
    def __init__(self, parent):
        """
        Inicializácia komponenty ResultsViewer.
        
        Args:
            parent: Rodičovský widget
        """
        super().__init__(parent)
        self.parent = parent
        
        # Inicializácia premenných
        self.excel_path = None
        self.results = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Nastavenie užívateľského rozhrania."""
        # Frame pre treeview
        treeview_frame = ttk.Frame(self)
        treeview_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Vytvorenie treeview pre zobrazenie výsledkov
        self.results_tree = ttk.Treeview(
            treeview_frame,
            columns=("file", "date", "total", "store"),
            show="headings"
        )
        
        # Nastavenie stĺpcov
        self.results_tree.heading("file", text="Súbor")
        self.results_tree.heading("date", text="Dátum")
        self.results_tree.heading("total", text="Celková suma")
        self.results_tree.heading("store", text="Obchod")
        
        self.results_tree.column("file", width=200)
        self.results_tree.column("date", width=100)
        self.results_tree.column("total", width=100)
        self.results_tree.column("store", width=150)
        
        # Scrollbar pre treeview
        scrollbar = ttk.Scrollbar(treeview_frame, orient=tk.VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)
        
        # Umiestnenie treeview a scrollbaru
        self.results_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Frame pre informácie o Excel súbore
        excel_frame = ttk.Frame(self)
        excel_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Label pre zobrazenie cesty k Excel súboru
        self.excel_label = ttk.Label(excel_frame, text="Excel súbor: Nie je k dispozícii")
        self.excel_label.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo pre otvorenie Excel súboru
        self.open_excel_button = ttk.Button(
            excel_frame, 
            text="Otvoriť Excel", 
            command=self.open_excel,
            state=tk.DISABLED
        )
        self.open_excel_button.pack(side=tk.RIGHT, padx=5)
    
    def update_results(self, results, excel_path=None):
        """
        Aktualizácia zobrazených výsledkov.
        
        Args:
            results: Zoznam výsledkov spracovania
            excel_path: Cesta k vygenerovanému Excel súboru
        """
        # Vyčistenie treeview
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Aktualizácia premenných
        self.results = results
        self.excel_path = excel_path
        
        # Naplnenie treeview novými údajmi
        for result in results:
            self.results_tree.insert(
                "", 
                tk.END, 
                values=(
                    result.get("file", ""),
                    result.get("date", ""),
                    result.get("total", ""),
                    result.get("store", "")
                )
            )
        
        # Aktualizácia informácií o Excel súbore
        if excel_path and os.path.exists(excel_path):
            self.excel_label.config(text=f"Excel súbor: {excel_path}")
            self.open_excel_button.config(state=tk.NORMAL)
        else:
            self.excel_label.config(text="Excel súbor: Nie je k dispozícii")
            self.open_excel_button.config(state=tk.DISABLED)
    
    def open_excel(self):
        """Otvorenie vygenerovaného Excel súboru."""
        if not self.excel_path or not os.path.exists(self.excel_path):
            logger.warning("Excel súbor neexistuje: %s", self.excel_path)
            return
        
        try:
            # Otvorenie súboru v predvolenom programe podľa operačného systému
            if platform.system() == "Windows":
                os.startfile(self.excel_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", self.excel_path], check=True)
            else:  # Linux a ostatné
                subprocess.run(["xdg-open", self.excel_path], check=True)
            
            logger.info("Excel súbor otvorený: %s", self.excel_path)
        except Exception as e:
            logger.error("Chyba pri otváraní Excel súboru: %s", e)
    
    def clear(self):
        """Vyčistenie zobrazených výsledkov."""
        # Vyčistenie treeview
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Reset premenných
        self.results = []
        self.excel_path = None
        
        # Aktualizácia UI
        self.excel_label.config(text="Excel súbor: Nie je k dispozícii")
        self.open_excel_button.config(state=tk.DISABLED)
