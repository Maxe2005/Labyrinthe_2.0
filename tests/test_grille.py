import os
from labyrinthe.core.grille import Grille


def test_charger_depuis_fichier(tmp_path):
    # Création d'un fichier temporaire de labyrinthe
    contenu = """
0110
0100
0111
0000
""".strip()
    chemin = tmp_path / "lab.txt"
    with open(chemin, "w") as f:
        f.write(contenu)
    g = Grille()
    g.charger_depuis_fichier(str(chemin))
    assert g.lab == [[0, 1, 1, 0], [0, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]
    assert g.x == 4
    assert g.y == 4
