import Tkinter as tk

def saisir_grille():
    """
    Permet a l'utilisateur de saisir une grille de Sudoku dans une interface graphique.
    Retourne une liste de listes representant la grille.
    """
    def recuperer_grille():
        """
        Recupere les valeurs des cases apres validation.
        """
        for i in range(9):
            for j in range(9):
                val = entrees[i][j].get()
                grille[i][j] = int(val) if val.isdigit() else 0
        root.destroy()  # Ferme la fenetre une fois la grille recuperee

    root = tk.Tk()
    root.title("Saisir une grille de Sudoku")

    grille = [[0] * 9 for _ in range(9)]
    entrees = []

    # Creation des champs d'entree
    for i in range(9):
        ligne = []
        for j in range(9):
            entree = tk.Entry(root, width=2, font=("Helvetica", 18), justify="center")
            entree.grid(row=i, column=j, padx=5, pady=5)
            ligne.append(entree)
        entrees.append(ligne)

    # Bouton pour valider la grille
    bouton_valider = tk.Button(root, text="Valider", command=recuperer_grille)
    bouton_valider.grid(row=9, column=0, columnspan=9, pady=10)

    root.mainloop()
    return grille


def afficher_grille(root, grille):
    
    # Creation de la fenetre principale
    root.title("Grille de Sudoku")

    # Dimensions de la grille
    taille_case = 50
    taille_grille = taille_case * 9

    # Creation d'un canevas pour dessiner la grille
    canvas = tk.Canvas(root, width=taille_grille, height=taille_grille, bg="white")
    canvas.pack()

    # Dessiner les lignes de la grille
    for i in range(10): #0-9
        # Epaissir les lignes pour les blocs 3x3
        epaisseur = 3 if i % 3 == 0 else 1

        # Lignes horizontales
        canvas.create_line(0, i * taille_case, taille_grille, i * taille_case, width=epaisseur)

        # Lignes verticales
        canvas.create_line(i * taille_case, 0, i * taille_case, taille_grille, width=epaisseur)

    # Ajouter les chiffres dans les cases
    for i in range(9):
        for j in range(9):
            if grille[i][j] != 0:  # Si la case n'est pas vide
                canvas.create_text(
                    j * taille_case + taille_case // 2,
                    i * taille_case + taille_case // 2,
                    text=str(grille[i][j]),
                    font=("Helvetica", 16),
                    fill="black"
                )
