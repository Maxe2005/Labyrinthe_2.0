"""
Fenêtre principale de l'application Labyrinthe (Tkinter).
"""
import tkinter as tk
from Outils_Tkinter import Fenetre


class Laby_fen (Fenetre):
    def __init__(self, x=1000, y=800):
        tk.Tk.__init__(self)
        self.x = x  # = self.winfo_screenwidth() -200
        self.y = y  # = self.winfo_screenheight() -100
        self.title("The Labyrinthe")
        self.geometry(str(self.x) + "x" + str(self.y))
        self.min_x = 500
        self.min_y = 400
        self.minsize(self.min_x, self.min_y)
        self.init_config_grid()
        # self.bind("<Button-3>", self.redimentionner)

    def init_config_grid(self):
        self.poids_canvas_x = 9
        self.poids_canvas_y = 9
        self.poids_barre_laterale_droite_x = 1
        self.poids_barre_top_y = 1
        self.poids_total_x = self.poids_canvas_x + self.poids_barre_laterale_droite_x
        self.poids_total_y = self.poids_canvas_y + self.poids_barre_top_y

        self.grid_columnconfigure(0, weight=self.poids_canvas_x)
        self.grid_columnconfigure(1, weight=self.poids_barre_laterale_droite_x)
        self.grid_rowconfigure(0, weight=self.poids_barre_top_y)
        self.grid_rowconfigure(1, weight=self.poids_canvas_y)

    def redimentionner(self, event=None):
        pass
