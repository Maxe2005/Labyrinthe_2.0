# Labyrinthe 2.0

Projet Python pour la création, la gestion et la résolution de labyrinthes.

## Structure du projet

- `labyrinthe/` : code source principal
- `tests/` : tests unitaires
- `requirements.txt` : dépendances
- `Makefile` : commandes utiles

## Installation

### VENV

```bash
sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
```

### Dépendences

```bash
pip install -r requirements.txt
```

Si besoin (Souvent sur les systèmes Ubuntu/Debian):

```bash
sudo apt install python3-tk
```

## Lancement

```bash
python -m labyrinthe.main
```

ou bien :

```bash
make run
```
