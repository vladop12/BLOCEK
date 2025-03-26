#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Konfiguračný súbor pre aplikáciu BLOCEK.
"""

import os
from pathlib import Path

# Základné cesty
BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
TEMPLATES_DIR = os.path.join(RESOURCES_DIR, "templates")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Konfigurácia API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Konfigurácia súborov
SUPPORTED_IMAGE_FORMATS = [".jpg", ".jpeg", ".png"]
SUPPORTED_DOCUMENT_FORMATS = [".pdf"]
SUPPORTED_FORMATS = SUPPORTED_IMAGE_FORMATS + SUPPORTED_DOCUMENT_FORMATS

# Konfigurácia Excel
DEFAULT_EXCEL_FILENAME = "receipts_data.xlsx"

# Konfigurácia XML
XML_TEMPLATE_PATH = os.path.join(TEMPLATES_DIR, "xml_template.xml")

# Konfigurácia logovanie
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.join(LOGS_DIR, "blocek.log")

# Konfigurácia UI
UI_TITLE = "BLOCEK - Spracovanie pokladničných blokov"
UI_WIDTH = 800
UI_HEIGHT = 600