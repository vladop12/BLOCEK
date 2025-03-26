#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BLOCEK - Automatizovaný systém na spracovanie pokladničných blokov

Hlavný vstupný bod aplikácie.
"""

import os
import sys
import logging
import tkinter as tk
from tkinter import messagebox

# Pridanie adresára src do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from config import LOG_LEVEL, LOG_FORMAT, LOG_FILE, UI_TITLE, UI_WIDTH, UI_HEIGHT

# Nastavenie logovania
if not os.path.exists(os.path.dirname(LOG_FILE)):
    os.makedirs(os.path.dirname(LOG_FILE))

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Hlavná funkcia aplikácie."""
    try:
        # Import UI komponentov
        from src.ui.main_window import MainWindow
        
        # Vytvorenie hlavného okna aplikácie
        root = tk.Tk()
        root.title(UI_TITLE)
        root.geometry(f"{UI_WIDTH}x{UI_HEIGHT}")
        
        # Vytvorenie a spustenie aplikácie
        app = MainWindow(root)
        logger.info("Aplikácia bola úspešne spustená")
        root.mainloop()
        
    except Exception as e:
        logger.error(f"Chyba pri spustení aplikácie: {e}", exc_info=True)
        messagebox.showerror("Chyba", f"Nastala chyba pri spustení aplikácie: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()