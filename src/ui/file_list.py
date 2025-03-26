#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FileList - Komponenta pre zobrazenie a výber súborov na spracovanie.
"""

import os
import tkinter as tk
from tkinter import ttk
import logging

logger = logging.getLogger(__name__)

class FileList(ttk.Frame):
    """
    Komponenta pre zobrazenie a výber súborov na spracovanie.
    
    Atribúty:
        parent: Rodičovský widget
        files: Zoznam súborov v aktuálnom adresári
        select_all_var: BooleanVar pre checkbox "Vybrať všetky"
    """
    
    def __init__(self, parent):
        """
        Inicializácia komponenty FileList.
        
        Args:
            parent: Rodičovský widget
        """
        super().__init__(parent)
        self.parent = parent
        self.files = []
        self.select_all_var = tk.BooleanVar(value=False)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Nastavenie užívateľského rozhrania."""
        # Label
        ttk.Label(self, text="Zoznam súborov:").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        
        # Frame pre treeview a scrollbar
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        columns = ("filename", "type", "size")
        self.tree = ttk.Treeview(
            tree_frame, columns=columns, show="headings", selectmode="extended",
            yscrollcommand=scrollbar.set
        )
        
        # Nastavenie stĺpcov
        self.tree.heading("filename", text="Názov súboru")
        self.tree.heading("type", text="Typ")
        self.tree.heading("size", text="Veľkosť")
        
        self.tree.column("filename", width=300)
        self.tree.column("type", width=100)
        self.tree.column("size", width=100)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Prepojenie scrollbaru s treeview
        scrollbar.config(command=self.tree.yview)
        
        # Checkbox "Vybrať všetky"
        select_all_check = ttk.Checkbutton(
            self, text="Vybrať všetky", variable=self.select_all_var,
            command=self.toggle_select_all
        )
        select_all_check.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        # Nastavenie roztiahnutia riadkov a stĺpcov
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
    
    def update_file_list(self, directory):
        """
        Aktualizácia zoznamu súborov podľa vybraného adresára.
        
        Args:
            directory (str): Cesta k adresáru
        """
        # Vyčistenie treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Vyčistenie zoznamu súborov
        self.files = []
        
        # Ak adresár neexistuje, skončíme
        if not os.path.isdir(directory):
            logger.warning(f"Adresár {directory} neexistuje")
            return
        
        # Získanie zoznamu súborov v adresári
        try:
            all_files = os.listdir(directory)
            
            # Filtrovanie súborov podľa podporovaných formátov
            for filename in all_files:
                file_path = os.path.join(directory, filename)
                
                # Kontrola, či je to súbor
                if os.path.isfile(file_path):
                    # Získanie prípony súboru
                    _, ext = os.path.splitext(filename)
                    
                    # Získanie veľkosti súboru
                    size = os.path.getsize(file_path)
                    size_str = self._format_size(size)
                    
                    # Pridanie súboru do treeview
                    self.tree.insert(
                        "", tk.END, values=(filename, ext, size_str),
                        tags=(file_path,)
                    )
                    
                    # Pridanie súboru do zoznamu
                    self.files.append(file_path)
            
            logger.info(f"Načítaných {len(self.files)} súborov z adresára {directory}")
        
        except Exception as e:
            logger.error(f"Chyba pri načítavaní súborov z adresára {directory}: {e}")
    
    def get_selected_files(self):
        """
        Získanie zoznamu vybraných súborov.
        
        Returns:
            list: Zoznam ciest k vybraným súborom
        """
        selected_items = self.tree.selection()
        selected_files = []
        
        for item in selected_items:
            file_path = self.tree.item(item, "tags")[0]
            selected_files.append(file_path)
        
        return selected_files
    
    def toggle_select_all(self):
        """Prepínanie výberu všetkých súborov."""
        if self.select_all_var.get():
            # Vybrať všetky súbory
            self.tree.selection_set(self.tree.get_children())
        else:
            # Zrušiť výber všetkých súborov
            self.tree.selection_remove(self.tree.get_children())
    
    def _format_size(self, size_bytes):
        """
        Formátovanie veľkosti súboru.
        
        Args:
            size_bytes (int): Veľkosť súboru v bajtoch
            
        Returns:
            str: Formátovaná veľkosť súboru
        """
        # Konverzia na KB, MB, GB
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
