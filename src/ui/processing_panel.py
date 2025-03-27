#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ProcessingPanel - Komponenta pre spracovanie vybraných súborov a zobrazenie stavu spracovania.
"""

import tkinter as tk
from tkinter import ttk
import logging

logger = logging.getLogger(__name__)

class ProcessingPanel(ttk.Frame):
    """
    Komponenta pre spracovanie vybraných súborov a zobrazenie stavu spracovania.
    
    Atribúty:
        parent: Rodičovský widget
        process_callback: Callback funkcia volaná po kliknutí na tlačidlo "Spracovať"
        generate_xml_callback: Callback funkcia volaná po kliknutí na tlačidlo "Generovať XML"
    """
    
    def __init__(self, parent, process_callback=None, generate_xml_callback=None):
        """
        Inicializácia komponenty ProcessingPanel.
        
        Args:
            parent: Rodičovský widget
            process_callback: Callback funkcia volaná po kliknutí na tlačidlo "Spracovať"
            generate_xml_callback: Callback funkcia volaná po kliknutí na tlačidlo "Generovať XML"
        """
        super().__init__(parent)
        self.parent = parent
        self.process_callback = process_callback
        self.generate_xml_callback = generate_xml_callback
        
        # Inicializácia premenných
        self.progress_var = tk.DoubleVar(value=0)
        self.status_var = tk.StringVar(value="Pripravené na spracovanie")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Nastavenie užívateľského rozhrania."""
        # Frame pre tlačidlá
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Tlačidlo "Spracovať vybrané súbory"
        self.process_button = ttk.Button(
            button_frame, 
            text="Spracovať vybrané súbory", 
            command=self.on_process_button_click
        )
        self.process_button.pack(side=tk.LEFT, padx=5)
        
        # Tlačidlo "Generovať XML"
        self.generate_xml_button = ttk.Button(
            button_frame, 
            text="Generovať XML", 
            command=self.on_generate_xml_button_click,
            state=tk.DISABLED  # Na začiatku je tlačidlo zakázané
        )
        self.generate_xml_button.pack(side=tk.RIGHT, padx=5)
        
        # Frame pre progress bar a status
        progress_frame = ttk.Frame(self)
        progress_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            progress_frame, 
            variable=self.progress_var, 
            maximum=100, 
            mode='determinate'
        )
        self.progress_bar.pack(fill=tk.X, padx=5, pady=5)
        
        # Status label
        self.status_label = ttk.Label(
            progress_frame, 
            textvariable=self.status_var, 
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X, padx=5)
    
    def on_process_button_click(self):
        """Callback metóda volaná po kliknutí na tlačidlo "Spracovať"."""
        logger.info("Tlačidlo 'Spracovať vybrané súbory' bolo stlačené")
        if self.process_callback:
            self.process_callback()
    
    def on_generate_xml_button_click(self):
        """Callback metóda volaná po kliknutí na tlačidlo "Generovať XML"."""
        logger.info("Tlačidlo 'Generovať XML' bolo stlačené")
        if self.generate_xml_callback:
            self.generate_xml_callback()
    
    def update_progress(self, value, max_value):
        """
        Aktualizácia progress baru.
        
        Args:
            value: Aktuálna hodnota
            max_value: Maximálna hodnota
        """
        if max_value > 0:
            percentage = (value / max_value) * 100
            self.progress_var.set(percentage)
            self.update_idletasks()
    
    def update_status(self, status):
        """
        Aktualizácia stavu spracovania.
        
        Args:
            status: Nový stav
        """
        self.status_var.set(status)
        self.update_idletasks()
    
    def enable_buttons(self, enable=True):
        """
        Povolenie/zakázanie tlačidiel počas spracovania.
        
        Args:
            enable: True pre povolenie, False pre zakázanie
        """
        state = tk.NORMAL if enable else tk.DISABLED
        self.process_button.config(state=state)
    
    def enable_xml_button(self, enable=True):
        """
        Povolenie/zakázanie tlačidla "Generovať XML".
        
        Args:
            enable: True pre povolenie, False pre zakázanie
        """
        state = tk.NORMAL if enable else tk.DISABLED
        self.generate_xml_button.config(state=state)
    
    def reset(self):
        """Reset komponenty do počiatočného stavu."""
        self.progress_var.set(0)
        self.status_var.set("Pripravené na spracovanie")
        self.enable_buttons(True)
        self.enable_xml_button(False)
