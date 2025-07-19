from .Outils_Tkinter import Entite_superieure
from .gui import Laby_fen


class app(Entite_superieure):
    def __init__(self) -> None:
        """Constructeur, initialise les instances"""
        self.init_variables_globales()

        self.fenetre = Laby_fen()

    def lancement(self):
        """Permet de lancer la fenêtre du jeu"""
        self.lancement_fenetre()

    def init_variables_globales(self):
        """Permet de donner des valeurs arbitraires aux paramètres globaux (params par défaut)"""
        # self.ouvrir_param_defaut("Autres/Parametres_defaut.csv", "parcoureur")
        self.type_lab = "classique"
        self.commentaires = []
        # self.type_deplacement = self.parametres["type deplacement initial"]
        self.init_variables_tres_globales()


if __name__ == "__main__":
    fen_lab = app()
    fen_lab.lancement()
