import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Jednoduchý test")
    root.geometry("300x200")
    
    label = ttk.Label(root, text="Toto je testovací skript")
    label.pack(padx=20, pady=20)
    
    button = ttk.Button(root, text="Zavrieť", command=root.destroy)
    button.pack(pady=10)
    
    print("Testovací skript spustený")
    root.mainloop()
    print("Testovací skript ukončený")

if __name__ == "__main__":
    main()
