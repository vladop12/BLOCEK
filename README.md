# BLOCEK

Aplikácia na spracovanie pokladničných blokov a extrakciu údajov.

## Popis projektu

BLOCEK je desktopová aplikácia, ktorá umožňuje používateľom:
- Načítať obrázky pokladničných blokov
- Extrahovať z nich relevantné údaje pomocou OCR
- Organizovať a analyzovať tieto údaje
- Exportovať výsledky do rôznych formátov (Excel, XML)

## Inštalácia

### Požiadavky
- Python 3.11 alebo novší
- Pip (správca Python balíčkov)

### Postup inštalácie

1. Naklonujte repozitár:
```bash
git clone https://github.com/vladop12/BLOCEK.git
cd BLOCEK
```

2. Vytvorte virtuálne prostredie (odporúčané):
```bash
python -m venv venv
```

3. Aktivujte virtuálne prostredie:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/macOS:
   ```bash
   source venv/bin/activate
   ```

4. Nainštalujte závislosti:
```bash
pip install -r requirements.txt
```

## Spustenie aplikácie

```bash
python -m src.main
```

## Spustenie testov

```bash
python -m unittest discover tests
```

## Štruktúra projektu

- `src/` - zdrojový kód aplikácie
  - `ui/` - komponenty používateľského rozhrania
  - `processing/` - logika spracovania blokov
  - `models/` - dátové modely
  - `utils/` - pomocné funkcie a nástroje
- `tests/` - testy
- `docs/` - dokumentácia
- `resources/` - statické zdroje

## Prispievanie k projektu

1. Vytvorte fork repozitára
2. Vytvorte feature branch (`git checkout -b feature/amazing-feature`)
3. Commitnite vaše zmeny (`git commit -m 'Add some amazing feature'`)
4. Pushnite branch (`git push origin feature/amazing-feature`)
5. Otvorte Pull Request

## Licencia

[MIT](LICENSE)
```

## 3. Vytvorenie .gitignore

```:.gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Project specific
temp/
output/
*.xlsx
*.xml
```

## 4. Vytvorenie requirements.txt

```:requirements.txt
# GUI
tkinter

# Data processing
pandas
numpy
openpyxl

# OCR (bude implementované)
# pytesseract
# pillow

# Testing
pytest
```

## 5. Vytvorenie adresárovej štruktúry a základných súborov

### src/processing/__init__.py

```python:src/processing/__init__.py
"""
Modul pre spracovanie pokladničných blokov.
Obsahuje funkcie a triedy pre OCR a extrakciu údajov.
"""
```

### src/processing/ocr.py

```python:src/processing/ocr.py
"""
Modul pre OCR (Optical Character Recognition).
Poskytuje funkcie pre rozpoznávanie textu z obrázkov pokladničných blokov.
"""

class OCRProcessor:
    """
    Trieda pre spracovanie obrázkov pomocou OCR.
    """
    
    def __init__(self, config=None):
        """
        Inicializácia OCR procesora.
        
        Args:
            config (dict, optional): Konfigurácia OCR. Defaults to None.
        """
        self.config = config or {}
        # TODO: Inicializácia OCR enginu (napr. Tesseract)
    
    def process_image(self, image_path):
        """
        Spracovanie obrázku a extrakcia textu.
        
        Args:
            image_path (str): Cesta k obrázku.
            
        Returns:
            str: Extrahovaný text z obrázku.
        """
        # TODO: Implementácia OCR
        # Momentálne vrátime simulovaný výstup
        return f"Simulovaný OCR výstup pre {image_path}"
```

### src/models/__init__.py

```python:src/models/__init__.py
"""
Modul pre dátové modely aplikácie.
Obsahuje triedy reprezentujúce entity ako pokladničný blok, položka, atď.
"""
```

### src/models/receipt.py

```python:src/models/receipt.py
"""
Modul pre reprezentáciu pokladničného bloku a jeho položiek.
"""

from datetime import datetime

class ReceiptItem:
    """
    Trieda reprezentujúca položku na pokladničnom bloku.
    """
    
    def __init__(self, name, quantity, unit_price, total_price):
        """
        Inicializácia položky.
        
        Args:
            name (str): Názov položky.
            quantity (float): Množstvo.
            unit_price (float): Jednotková cena.
            total_price (float): Celková cena.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price
    
    def __str__(self):
        return f"{self.name} - {self.quantity} x {self.unit_price} = {self.total_price}"


class Receipt:
    """
    Trieda reprezentujúca pokladničný blok.
    """
    
    def __init__(self, store_name, date, total_amount, items=None):
        """
        Inicializácia pokladničného bloku.
        
        Args:
            store_name (str): Názov obchodu.
            date (datetime): Dátum nákupu.
            total_amount (float): Celková suma.
            items (list, optional): Zoznam položiek. Defaults to None.
        """
        self.store_name = store_name
        self.date = date
        self.total_amount = total_amount
        self.items = items or []
    
    def add_item(self, item):
        """
        Pridanie položky do pokladničného bloku.
        
        Args:
            item (ReceiptItem): Položka na pridanie.
        """
        self.items.append(item)
    
    def __str__(self):
        return f"{self.store_name} - {self.date.strftime('%d.%m.%Y')} - {self.total_amount} €"
```

### src/utils/__init__.py

```python:src/utils/__init__.py
"""
Modul pre pomocné funkcie a nástroje.
"""
```

### src/utils/file_utils.py

```python:src/utils/file_utils.py
"""
Modul pre prácu so súbormi.
"""

import os
import shutil
from pathlib import Path

def get_file_extension(file_path):
    """
    Získanie prípony súboru.
    
    Args:
        file_path (str): Cesta k súboru.
        
    Returns:
        str: Prípona súboru.
    """
    return os.path.splitext(file_path)[1].lower()

def is_image_file(file_path):
    """
    Kontrola, či je súbor obrázok.
    
    Args:
        file_path (str): Cesta k súboru.
        
    Returns:
        bool: True ak je súbor obrázok, inak False.
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']
    return get_file_extension(file_path) in image_extensions

def create_directory_if_not_exists(directory_path):
    """
    Vytvorenie adresára, ak neexistuje.
    
    Args:
        directory_path (str): Cesta k adresáru.
    """
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def copy_file(source_path, destination_path):
    """
    Kopírovanie súboru.
    
    Args:
        source_path (str): Zdrojová cesta.
        destination_path (str): Cieľová cesta.
    """
    shutil.copy2(source_path, destination_path)
```

### src/utils/export_utils.py

```python:src/utils/export_utils.py
"""
Modul pre export dát do rôznych formátov.
"""

import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def export_to_excel(data, file_path):
    """
    Export dát do Excel súboru.
    
    Args:
        data (list): Dáta na export.
        file_path (str): Cesta k výstupnému súboru.
    """
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

def export_to_xml(data, file_path):
    """
    Export dát do XML súboru.
    
    Args:
        data (list): Dáta na export.
        file_path (str): Cesta k výstupnému súboru.
    """
    root = ET.Element("receipts")
    
    for receipt_data in data:
        receipt = ET.SubElement(root, "receipt")
        
        for key, value in receipt_data.items():
            if key == "items":
                items_element = ET.SubElement(receipt, "items")
                for item in value:
                    item_element = ET.SubElement(items_element, "item")
                    for item_key, item_value in item.items():
                        ET.SubElement(item_element, item_key).text = str(item_value)
            else:
                ET.SubElement(receipt, key).text = str(value)
    
    # Formátovanie XML pre lepšiu čitateľnosť
    xml_string = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
```

### resources/README.md

```markdown:resources/README.md
# Zdroje

Tento adresár obsahuje statické zdroje pre aplikáciu:

- Ikony
- Obrázky
- Vzorové dáta
- Konfiguračné súbory

## Štruktúra

- `icons/` - ikony aplikácie
- `images/` - obrázky používané v aplikácii
- `samples/` - vzorové pokladničné bloky pre testovanie
- `config/` - konfiguračné súbory
