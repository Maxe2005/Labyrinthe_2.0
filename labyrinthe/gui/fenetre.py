"""
Fenêtre principale de l'application Labyrinthe (Tkinter).
"""
import tkinter as tk
from .canvas import LabyrintheCanvas

class Fenetre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Labyrinthe 2.0")
        self.geometry("1000x800")
        self.minsize(500, 400)
        self.canvas = LabyrintheCanvas(self)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        # TODO: Ajouter barres, boutons, etc.
