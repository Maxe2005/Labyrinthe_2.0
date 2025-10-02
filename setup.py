from setuptools import setup, find_packages

setup(
    name="labyrinthe",
    version="0.1.0",
    description="Projet Python pour la création, la gestion et la résolution de labyrinthes.",
    author="Maxubu",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "pytest",
        "flake8",
        "black",
    ],
    python_requires=">=3.8",
)
