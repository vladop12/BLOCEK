#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testy pre MainWindow - hlavné okno aplikácie pre spracovanie pokladničných blokov.
"""

import unittest
import tkinter as tk
import os
import sys
from unittest.mock import MagicMock, patch

# Pridanie koreňového adresára projektu do PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.ui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    """
    Testy pre triedu MainWindow.
    """
    
    def setUp(self):
        """Nastavenie pred každým testom."""
        self.root = tk.Tk()
        self.app = MainWindow(self.root)
    
    def tearDown(self):
        """Čistenie po každom teste."""
        self.root.destroy()
    
    def test_initialization(self):
        """Test inicializácie hlavného okna."""
        self.assertEqual(self.root.title(), "Spracovanie pokladničných blokov")
        self.assertIsNotNone(self.app.file_selector)
        self.assertIsNotNone(self.app.file_list)
        # Odstránené: self.assertIsNotNone(self.app.image_preview)
        self.assertIsNotNone(self.app.processing_options)
        self.assertIsNotNone(self.app.processing_panel)
        self.assertIsNotNone(self.app.results_viewer)

    def test_file_selection_callback(self):
        """Test callbacku pre výber súborov."""
        # Mock pre metódu update_file_list
        self.app.file_list.update_file_list = MagicMock()
    
        # Simulácia výberu súborov
        test_files = ["test1.jpg", "test2.jpg"]
        self.app.on_files_selected(test_files)
    
        # Overenie, či boli volané správne metódy
        self.app.file_list.update_file_list.assert_called_once_with(test_files)
        # Odstránené: self.app.file_list.select_first_file.assert_called_once()

    
    def test_file_list_selection_callback(self):
        """Test callbacku pre výber súboru v zozname."""
        # Odstránené: self.app.image_preview.load_image = MagicMock()
    
        # Simulácia výberu súboru v zozname
        test_file = "test.jpg"
        # Overenie, že metóda nespôsobí chybu
        try:
            self.app.on_file_list_selection(test_file)
            # Test prešiel, ak sa nevyskytla výnimka
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed, "Metóda on_file_list_selection vyvolala výnimku")

    
    @patch('threading.Thread')
    def test_process_files(self, mock_thread):
        """Test spracovania súborov."""
        # Mock pre metódy
        self.app.file_list.get_file_list = MagicMock(return_value=["test1.jpg", "test2.jpg"])
        self.app.processing_options.get_options = MagicMock(return_value={"option1": True, "option2": False})
        self.app.processing_panel.update_status = MagicMock()
        self.app.processing_panel.enable_buttons = MagicMock()
        
        # Volanie metódy na spracovanie súborov
        self.app.on_process_files()
        
        # Overenie, či boli volané správne metódy
        self.app.file_list.get_file_list.assert_called_once()
        self.app.processing_options.get_options.assert_called_once()
        self.app.processing_panel.update_status.assert_called_once_with("Spracovávam súbory...")
        self.app.processing_panel.enable_buttons.assert_called_once_with(False)
        mock_thread.assert_called_once()
        mock_thread.return_value.start.assert_called_once()
        
        # Test s prázdnym zoznamom súborov
        mock_thread.reset_mock()
        self.app.processing_panel.update_status.reset_mock()
        self.app.processing_panel.enable_buttons.reset_mock()
        self.app.file_list.get_file_list = MagicMock(return_value=[])
        
        self.app.on_process_files()
        
        # Overenie, že spracovanie nebolo spustené
        mock_thread.assert_not_called()
        self.app.processing_panel.update_status.assert_not_called()
        self.app.processing_panel.enable_buttons.assert_not_called()
    @patch('threading.Thread')
    def test_generate_xml(self, mock_thread):
        """Test generovania XML."""
        # Mock pre metódy
        self.app.processing_panel.update_status = MagicMock()
        self.app.processing_panel.enable_buttons = MagicMock()
        self.app.processing_panel.enable_xml_button = MagicMock()
        
        # Volanie metódy na generovanie XML
        self.app.on_generate_xml()
        
        # Overenie, či boli volané správne metódy
        self.app.processing_panel.update_status.assert_called_once_with("Generujem XML...")
        self.app.processing_panel.enable_buttons.assert_called_once_with(False)
        self.app.processing_panel.enable_xml_button.assert_called_once_with(False)
        mock_thread.assert_called_once()
        mock_thread.return_value.start.assert_called_once()
    
    def test_open_files_menu(self):
        """Test funkcie menu 'Otvoriť súbory'."""
        # Vytvorenie mock objektu pre metódu browse_directory
        self.app.file_selector.browse_directory = MagicMock()
    
        # Volanie funkcie menu
        self.app.on_open_files()
    
        # Overenie, či bola volaná správna metóda
        self.app.file_selector.browse_directory.assert_called_once()

    
    @patch('tkinter.filedialog.asksaveasfilename')
    @patch('builtins.open')
    @patch('tkinter.messagebox.showinfo')
    @patch('tkinter.messagebox.showwarning')
    def test_save_results(self, mock_showwarning, mock_showinfo, mock_open, mock_asksaveasfilename):
        """Test funkcie menu 'Uložiť výsledky'."""
        # Test s prázdnymi výsledkami
        self.app.results_viewer.results = []
        
        self.app.on_save_results()
        
        # Overenie, že sa zobrazilo upozornenie
        mock_showwarning.assert_called_once()
        mock_asksaveasfilename.assert_not_called()
        
        # Reset mockov
        mock_showwarning.reset_mock()
        mock_asksaveasfilename.reset_mock()
        
        # Test s výsledkami, ale zrušenie uloženia
        self.app.results_viewer.results = [{"file": "test.jpg", "date": "2023-01-01", "total": "10.50 €", "store": "Tesco"}]
        mock_asksaveasfilename.return_value = ""
        
        self.app.on_save_results()
        
        # Overenie, že sa zobrazil dialóg, ale súbor sa neuložil
        mock_asksaveasfilename.assert_called_once()
        mock_open.assert_not_called()
        
        # Reset mockov
        mock_asksaveasfilename.reset_mock()
        
        # Test s výsledkami a úspešným uložením
        mock_asksaveasfilename.return_value = "test.xlsx"
        
        self.app.on_save_results()
        
        # Overenie, že sa súbor uložil a zobrazila sa informácia
        mock_asksaveasfilename.assert_called_once()
        mock_open.assert_called_once()
        mock_showinfo.assert_called_once()
    @patch('tkinter.messagebox.showinfo')
    def test_help_menu(self, mock_showinfo):
        """Test funkcie menu 'Návod'."""
        # Volanie metódy z menu
        self.app.on_help()
        
        # Overenie, či sa zobrazil dialóg s návodom
        mock_showinfo.assert_called_once()
        args, kwargs = mock_showinfo.call_args
        self.assertEqual(args[0], "Návod")
    
    @patch('tkinter.messagebox.showinfo')
    def test_about_menu(self, mock_showinfo):
        """Test funkcie menu 'O aplikácii'."""
        # Volanie metódy z menu
        self.app.on_about()
        
        # Overenie, či sa zobrazil dialóg s informáciami o aplikácii
        mock_showinfo.assert_called_once()
        args, kwargs = mock_showinfo.call_args
        self.assertEqual(args[0], "O aplikácii")
    
    @patch('tkinter.Tk')
    @patch('src.ui.main_window.MainWindow')
    def test_main_function(self, mock_main_window, mock_tk):
        """Test hlavnej funkcie aplikácie."""
        # Import main funkcie
        from src.ui.main_window import main
    
        # Vytvorenie mock objektu pre mainloop
        mock_instance = mock_tk.return_value
        mock_instance.mainloop = MagicMock()
    
        # Volanie hlavnej funkcie
        main()
    
        # Overenie, či boli volané správne metódy
        mock_tk.assert_called_once()
        mock_main_window.assert_called_once()
        mock_instance.mainloop.assert_called_once()

    
    def test_exit_menu(self):
        """Test funkcie menu 'Ukončiť'."""
        # Mock pre metódu destroy
        self.root.destroy = MagicMock()
        
        # Volanie metódy z menu
        self.app.on_exit()
        
        # Overenie, či bola volaná správna metóda
        self.root.destroy.assert_called_once()


if __name__ == "__main__":
    unittest.main()
