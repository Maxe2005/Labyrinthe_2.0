"""
Canvas d'affichage du labyrinthe.
"""

import tkinter as tk
from ..Outils_Tkinter import Canvas


class Laby_canvas(Canvas):
    "Canvas d´affichage du labyrinthe"

    def __init__(self, column=0, row=1):
        super().__init__("black")
        self.grid(column=column, row=row, sticky=tk.NSEW)
