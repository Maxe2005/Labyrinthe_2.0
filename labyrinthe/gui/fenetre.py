"""
Fenêtre principale de l'application Labyrinthe (Tkinter).
"""
import tkinter as tk
from .canvas import LabyrintheCanvas



import tkinter.messagebox as messagebox

class Fenetre(tk.Tk):
    """
    Fenêtre principale de l'application Labyrinthe (Tkinter).
    Gère l'initialisation et affiche les erreurs critiques à l'utilisateur.
    """
    def __init__(self) -> None:
        try:
            super().__init__()
            self.title("Labyrinthe 2.0")
            self.geometry("1000x800")
            self.minsize(500, 400)
            self.main_frame = tk.Frame(self)
            self.main_frame.pack(expand=True, fill=tk.BOTH)
            self.canvas: LabyrintheCanvas = LabyrintheCanvas(self.main_frame)
            self.canvas.pack(expand=True, fill=tk.BOTH)
            # TODO: Ajouter barres, boutons, etc.
        except Exception as error:
            self.afficher_erreur(f"Erreur lors de l'initialisation de la fenêtre : {error}")

    def afficher_erreur(self, message: str) -> None:
        """
        Affiche une boîte de dialogue d'erreur à l'utilisateur.
        Args:
            message (str): Message à afficher.
        """
        messagebox.showerror("Erreur", message)
