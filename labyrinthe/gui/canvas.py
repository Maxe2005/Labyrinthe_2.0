"""
Canvas d'affichage du labyrinthe.
"""
import tkinter as tk


class LabyrintheCanvas(tk.Canvas):
    """
    Canvas d'affichage du labyrinthe.
    """
    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, bg='white')
        # TODO: Ajouter gestion du dessin de la grille et de la balle

    def dessiner_grille(self, grille: object) -> None:
        """
        Dessine la grille du labyrinthe.

        Args:
            grille (object): instance de la grille à dessiner.
        """
        # TODO: Implémenter le dessin
        pass

    def dessiner_balle(self, balle: object) -> None:
        """
        Dessine la balle sur le canvas.

        Args:
            balle (object): instance de la balle à dessiner.
        """
        # TODO: Implémenter le dessin
        pass
