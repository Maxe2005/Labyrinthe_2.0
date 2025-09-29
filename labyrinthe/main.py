from .Outils_Tkinter import Entite_superieure
from .gui import Laby_fen
from functools import partial


class app(Entite_superieure):
    def __init__(self) -> None:
        """Constructeur, initialise les instances"""
        self.init_variables_globales()

        self.fenetre = Laby_fen()

    def lancement(self):
        """Permet de lancer la fenêtre du jeu"""
        self.fenetre.focus()
        self.fenetre.protocol(
            "WM_DELETE_WINDOW", partial(self.on_closing, self.fenetre)
        )
        self.fenetre.mainloop()

    def init_variables_globales(self):
        """Permet de donner des valeurs arbitraires aux paramètres globaux (params par défaut)"""
        # self.ouvrir_param_defaut("Autres/Parametres_defaut.csv", "parcoureur")
        self.type_lab = "classique"
        self.commentaires = []

    def on_closing(self, objet_fenetre):
        "Permet de sauvegarder les changements effectués dans les réglages au moment de la fermeture de la fenêtre"
        objet_fenetre.destroy()


if __name__ == "__main__":
    fen_lab = app()
    fen_lab.lancement()
