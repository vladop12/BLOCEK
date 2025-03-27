"""
Modul pre načítanie premenných prostredia z .env súboru.
"""

import os
from pathlib import Path
import logging
import re

logger = logging.getLogger(__name__)

def load_env_file(env_file=None):
    """
    Načíta premenné prostredia z .env súboru.
    
    Args:
        env_file (str, optional): Cesta k .env súboru. Ak nie je zadaná,
            hľadá sa .env súbor v koreňovom adresári projektu.
    """
    if env_file is None:
        # Hľadanie .env súboru v koreňovom adresári projektu
        project_root = Path(__file__).parent.parent.parent
        env_file = project_root / '.env'
    
    if not os.path.exists(env_file):
        logger.warning(f".env súbor nebol nájdený na ceste: {env_file}")
        return
    
    logger.info(f"Načítavam premenné prostredia z: {env_file}")
    
    try:
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Použitie regulárneho výrazu pre bezpečné rozdelenie
                match = re.match(r'^([A-Za-z0-9_]+)=(.*)$', line)
                if match:
                    key, value = match.groups()
                    # Odstránenie úvodzoviek, ak existujú
                    value = value.strip('"\'')
                    os.environ[key] = value
                    logger.debug(f"Nastavená premenná prostredia: {key}")
                else:
                    logger.warning(f"Ignorujem neplatnú riadku v .env súbore: {line}")
        
        logger.info("Premenné prostredia boli úspešne načítané.")
    except Exception as e:
        logger.error(f"Chyba pri načítavaní .env súboru: {e}")
        raise
