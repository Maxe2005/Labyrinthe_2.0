"""
Module de gestion de la balle (joueur).
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .grille import Grille


class Balle:
    """
    Repr9sente la balle (joueur) dans le labyrinthe.

    Attributs :
        grille (Grille) : la grille du labyrinthe.
        x (int) : position x de la balle.
        y (int) : position y de la balle.
    """
    def __init__(self, grille: 'Grille', x: int = 0, y: int = 0) -> None:
        self.grille: 'Grille' = grille
        self.x: int = x
        self.y: int = y
        # TODO: Ajouter d'autres attributs n9cessaires

    def deplacer(self, direction: str) -> None:
        """
        D9place la balle dans la direction donn9e.

        Args:
            direction (str): 'haut', 'bas', 'gauche' ou 'droite'.
        """
        # TODO: Impl9menter le d9placement
        pass
