"""
Module de gestion de la balle (joueur).
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .grille import Grille

class Balle:
    """Représente la balle (joueur) dans le labyrinthe."""
    def __init__(self, grille: 'Grille', x: int = 0, y: int = 0):
        self.grille = grille
        self.x = x
        self.y = y
        # TODO: Ajouter d'autres attributs nécessaires

    def deplacer(self, direction: str) -> None:
        """Déplace la balle dans la direction donnée."""
        # TODO: Implémenter le déplacement
        pass
