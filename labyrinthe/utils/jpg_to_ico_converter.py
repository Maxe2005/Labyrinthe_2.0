from PIL import Image
import os
import sys


def convert_jpg_to_ico(
    input_path, output_path=None, sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
):
    """
    Convertit un fichier JPG en ICO

    Args:
        input_path (str): Chemin vers le fichier JPG
        output_path (str): Chemin de sortie pour le fichier ICO (optionnel)
        sizes (list): Liste des tailles à inclure dans l'ICO
    """
    try:
        # Ouvrir l'image JPG
        with Image.open(input_path) as img:
            # Convertir en RGBA si nécessaire (pour la transparence)
            if img.mode != "RGBA":
                img = img.convert("RGBA")

            # Définir le chemin de sortie si non spécifié
            if output_path is None:
                base_name = os.path.splitext(input_path)[0]
                output_path = f"{base_name}.ico"

            # Créer les différentes tailles
            icon_images = []
            for size in sizes:
                resized_img = img.resize(size, Image.Resampling.LANCZOS)
                icon_images.append(resized_img)

            # Sauvegarder comme fichier ICO
            icon_images[0].save(
                output_path,
                format="ICO",
                sizes=[(img.width, img.height) for img in icon_images],
            )

            print(f"✅ Conversion réussie: {input_path} -> {output_path}")
            return True

    except Exception as e:
        print(f"❌ Erreur lors de la conversion de {input_path}: {e}")
        return False


def convert_multiple_jpg_to_ico(input_folder, output_folder=None):
    """
    Convertit tous les fichiers JPG d'un dossier en ICO

    Args:
        input_folder (str): Dossier contenant les fichiers JPG
        output_folder (str): Dossier de sortie (optionnel)
    """
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    jpg_files = [
        f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg"))
    ]

    if not jpg_files:
        print("Aucun fichier JPG trouvé dans le dossier.")
        return

    converted = 0
    for jpg_file in jpg_files:
        input_path = os.path.join(input_folder, jpg_file)

        if output_folder:
            base_name = os.path.splitext(jpg_file)[0]
            output_path = os.path.join(output_folder, f"{base_name}.ico")
        else:
            output_path = None

        if convert_jpg_to_ico(input_path, output_path):
            converted += 1

    print(f"\n📊 Résumé: {converted}/{len(jpg_files)} fichiers convertis avec succès.")


def main():
    """Interface en ligne de commande"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python jpg_to_ico_converter.py <fichier.jpg>")
        print("  python jpg_to_ico_converter.py <dossier_input> [dossier_output]")
        return

    input_path = sys.argv[1]

    if os.path.isfile(input_path):
        # Convertir un seul fichier
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        convert_jpg_to_ico(input_path, output_path)

    elif os.path.isdir(input_path):
        # Convertir tous les fichiers d'un dossier
        output_folder = sys.argv[2] if len(sys.argv) > 2 else None
        convert_multiple_jpg_to_ico(input_path, output_folder)

    else:
        print(f"❌ Le chemin '{input_path}' n'existe pas.")


# Interface graphique simple avec tkinter
def create_gui():
    """Interface graphique pour la conversion"""
    import tkinter as tk
    from tkinter import filedialog, messagebox

    def select_file():
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier JPG",
            filetypes=[("Images JPG", "*.jpg *.jpeg"), ("Tous les fichiers", "*.*")],
        )
        if file_path:
            entry_input.delete(0, tk.END)
            entry_input.insert(0, file_path)

    def select_folder():
        folder_path = filedialog.askdirectory(title="Sélectionner un dossier")
        if folder_path:
            entry_input.delete(0, tk.END)
            entry_input.insert(0, folder_path)

    def convert():
        input_path = entry_input.get().strip()
        if not input_path:
            messagebox.showerror(
                "Erreur", "Veuillez sélectionner un fichier ou dossier."
            )
            return

        try:
            if os.path.isfile(input_path):
                success = convert_jpg_to_ico(input_path)
                if success:
                    messagebox.showinfo("Succès", "Conversion terminée avec succès!")
            elif os.path.isdir(input_path):
                convert_multiple_jpg_to_ico(input_path)
                messagebox.showinfo("Succès", "Conversion du dossier terminée!")
            else:
                messagebox.showerror("Erreur", "Le chemin spécifié n'existe pas.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la conversion: {e}")

    # Interface graphique
    root = tk.Tk()
    root.title("Convertisseur JPG vers ICO")
    root.geometry("500x200")

    # Widgets
    tk.Label(root, text="Convertisseur JPG vers ICO", font=("Arial", 14, "bold")).pack(
        pady=10
    )

    frame_input = tk.Frame(root)
    frame_input.pack(pady=10, padx=20, fill="x")

    tk.Label(frame_input, text="Fichier/Dossier:").pack(anchor="w")

    frame_entry = tk.Frame(frame_input)
    frame_entry.pack(fill="x", pady=5)

    entry_input = tk.Entry(frame_entry, width=50)
    entry_input.pack(side="left", fill="x", expand=True)

    tk.Button(frame_entry, text="Fichier", command=select_file).pack(
        side="right", padx=(5, 0)
    )
    tk.Button(frame_entry, text="Dossier", command=select_folder).pack(side="right")

    tk.Button(
        root,
        text="Convertir",
        command=convert,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12),
    ).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    # Lancer l'interface graphique si aucun argument en ligne de commande
    if len(sys.argv) == 1:
        print("Lancement de l'interface graphique...")
        create_gui()
    else:
        main()
