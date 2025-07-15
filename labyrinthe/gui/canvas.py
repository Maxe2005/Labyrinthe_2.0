"""
Canvas d'affichage du labyrinthe.
"""
import tkinter as tk

class LabyrintheCanvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, bg='white')
        # TODO: Ajouter gestion du dessin de la grille et de la balle

    def dessiner_grille(self, grille):
        """Dessine la grille du labyrinthe."""
        # TODO: Implémenter le dessin
        pass

    def dessiner_balle(self, balle):
        """Dessine la balle sur le canvas."""
        # TODO: Implémenter le dessin
        pass
