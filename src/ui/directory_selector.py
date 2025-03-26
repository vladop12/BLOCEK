#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DirectorySelector - Komponenta pre výber adresára s pokladničnými blokmi.
"""

import os
import tkinter as tk
from tkinter import filedialog, ttk

class DirectorySelector(ttk.Frame):
    """
    Komponenta pre výber adresára s pokladničnými blokmi.
    
    Atribúty:
        parent: Rodičovský widget
        callback: Callback funkcia volaná po výbere adresára
        directory_var: StringVar obsahujúci cestu k vybranému adresáru
    """
    
    def __init__(self, parent, callback=None):
        """
        Inicializácia komponenty DirectorySelector.
        
        Args:
            parent: Rodičovský widget
            callback: Callback funkcia volaná po výbere adresára
        """
        super().__init__(parent)
        self.parent = parent
        self.callback = callback
        self.directory_var = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Nastavenie užívateľského rozhrania."""
        # Label
        ttk.Label(self, text="Vyberte adresár s pokladničnými blokmi:").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        
        # Frame pre entry a tlačidlo
        entry_frame = ttk.Frame(self)
        entry_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        # Entry pre zobrazenie cesty
        self.directory_entry = ttk.Entry(
            entry_frame, textvariable=self.directory_var, width=50
        )
        self.directory_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        # Tlačidlo pre výber adresára
        browse_button = ttk.Button(
            entry_frame, text="Prehľadávať...", command=self.browse_directory
        )
        browse_button.grid(row=0, column=1, sticky="e")
        
        # Nastavenie roztiahnutia stĺpcov
        entry_frame.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
    
    def browse_directory(self):
        """Otvorenie dialógu na výber adresára."""
        directory = filedialog.askdirectory(
            title="Vyberte adresár s pokladničnými blokmi",
            initialdir=os.path.expanduser("~")
        )
        
        if directory:  # Ak používateľ vybral adresár (neklikol na Cancel)
            self.directory_var.set(directory)
            if self.callback:
                self.callback(directory)
    
    def get_directory(self):
        """
        Získanie aktuálne vybraného adresára.
        
        Returns:
            str: Cesta k vybranému adresáru
        """
        return self.directory_var.get()
