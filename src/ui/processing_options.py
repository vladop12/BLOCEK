#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ProcessingOptions - Komponenta pre nastavenie možností spracovania pokladničných blokov.
"""

import tkinter as tk
from tkinter import ttk
import logging

logger = logging.getLogger(__name__)

class ProcessingOptions(ttk.Frame):
    """
    Komponenta pre nastavenie možností spracovania pokladničných blokov.
    
    Atribúty:
        parent: Rodičovský widget
        output_format_var: StringVar pre výber formátu výstupu
        group_by_var: StringVar pre výber zoskupenia výsledkov
        include_tax_var: BooleanVar pre zahrnutie DPH do výsledkov
        categorize_var: BooleanVar pre kategorizáciu položiek
        date_range_var: BooleanVar pre filtrovanie podľa dátumu
        start_date_var: StringVar pre počiatočný dátum
        end_date_var: StringVar pre koncový dátum
    """
    
    def __init__(self, parent, callback=None):
        """
        Inicializácia komponenty ProcessingOptions.
        
        Args:
            parent: Rodičovský widget
            callback: Callback funkcia volaná po zmene nastavení
        """
        super().__init__(parent)
        self.parent = parent
        self.callback = callback
        
        # Premenné pre nastavenia
        self.output_format_var = tk.StringVar(value="csv")
        self.group_by_var = tk.StringVar(value="none")
        self.include_tax_var = tk.BooleanVar(value=True)
        self.categorize_var = tk.BooleanVar(value=False)
        self.date_range_var = tk.BooleanVar(value=False)
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Nastavenie užívateľského rozhrania."""
        # Hlavný nadpis
        ttk.Label(self, text="Možnosti spracovania:", font=("", 10, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=5, pady=(5, 10)
        )
        
        # Frame pre formát výstupu
        output_frame = ttk.LabelFrame(self, text="Formát výstupu")
        output_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        ttk.Radiobutton(
            output_frame, text="CSV", variable=self.output_format_var, value="csv",
            command=self._on_settings_changed
        ).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        
        ttk.Radiobutton(
            output_frame, text="Excel", variable=self.output_format_var, value="excel",
            command=self._on_settings_changed
        ).grid(row=1, column=0, sticky="w", padx=5, pady=2)
        
        ttk.Radiobutton(
            output_frame, text="JSON", variable=self.output_format_var, value="json",
            command=self._on_settings_changed
        ).grid(row=2, column=0, sticky="w", padx=5, pady=2)
        
        # Frame pre zoskupenie
        group_frame = ttk.LabelFrame(self, text="Zoskupenie výsledkov")
        group_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        
        ttk.Radiobutton(
            group_frame, text="Žiadne", variable=self.group_by_var, value="none",
            command=self._on_settings_changed
        ).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        
        ttk.Radiobutton(
            group_frame, text="Podľa dátumu", variable=self.group_by_var, value="date",
            command=self._on_settings_changed
        ).grid(row=1, column=0, sticky="w", padx=5, pady=2)
        
        ttk.Radiobutton(
            group_frame, text="Podľa obchodu", variable=self.group_by_var, value="store",
            command=self._on_settings_changed
        ).grid(row=2, column=0, sticky="w", padx=5, pady=2)
        
        # Frame pre ďalšie možnosti
        options_frame = ttk.LabelFrame(self, text="Ďalšie možnosti")
        options_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        ttk.Checkbutton(
            options_frame, text="Zahrnúť DPH do výsledkov", variable=self.include_tax_var,
            command=self._on_settings_changed
        ).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        
        ttk.Checkbutton(
            options_frame, text="Kategorizovať položky", variable=self.categorize_var,
            command=self._on_settings_changed
        ).grid(row=1, column=0, sticky="w", padx=5, pady=2)
        
        # Frame pre filtrovanie podľa dátumu
        date_frame = ttk.LabelFrame(self, text="Filtrovanie podľa dátumu")
        date_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Checkbox pre aktiváciu filtrovania podľa dátumu
        self.date_range_check = ttk.Checkbutton(
            date_frame, text="Filtrovať podľa dátumu", variable=self.date_range_var,
            command=self._on_date_range_changed
        )
        self.date_range_check.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        
        # Počiatočný dátum
        ttk.Label(date_frame, text="Od:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.start_date_entry = ttk.Entry(date_frame, textvariable=self.start_date_var, width=12)
        self.start_date_entry.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        self.start_date_entry.config(state="disabled")
        
        # Koncový dátum
        ttk.Label(date_frame, text="Do:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.end_date_entry = ttk.Entry(date_frame, textvariable=self.end_date_var, width=12)
        self.end_date_entry.grid(row=2, column=1, sticky="w", padx=5, pady=2)
        self.end_date_entry.config(state="disabled")
        
        # Nastavenie roztiahnutia riadkov a stĺpcov
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
    
    def _on_settings_changed(self):
        """Callback funkcia volaná po zmene nastavení."""
        if self.callback:
            self.callback(self.get_options())
    
    def _on_date_range_changed(self):
        """Callback funkcia volaná po zmene nastavenia filtrovania podľa dátumu."""
        if self.date_range_var.get():
            self.start_date_entry.config(state="normal")
            self.end_date_entry.config(state="normal")
        else:
            self.start_date_entry.config(state="disabled")
            self.end_date_entry.config(state="disabled")
        
        self._on_settings_changed()
    
    def get_options(self):
        """
        Získanie aktuálnych nastavení spracovania.
        
        Returns:
            dict: Slovník s aktuálnymi nastaveniami
        """
        options = {
            "output_format": self.output_format_var.get(),
            "group_by": self.group_by_var.get(),
            "include_tax": self.include_tax_var.get(),
            "categorize": self.categorize_var.get(),
            "date_range": {
                "enabled": self.date_range_var.get(),
                "start_date": self.start_date_var.get() if self.date_range_var.get() else None,
                "end_date": self.end_date_var.get() if self.date_range_var.get() else None
            }
        }
        
        return options
