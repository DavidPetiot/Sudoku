import Tkinter as tk

from builtins import range

def find_in_row(grille, line, value):
    res = False
    for i in range(9):
        if grille[i][line] == value:
            res = True
    return res

def find_in_col(grille, col, value):
    res = False
    for i in range(9):
        if grille[col][i] == value:
            res = True
    return res

def find_in_square(grille, row, col, value):
    res = False
    #determine square
    row_offset = 0 if row < 3 else 3 if row < 6 else 6
    col_offset = 0 if col < 3 else 3 if col < 6 else 6
    #row_offset, col_offset = 3 * (row // 3), 3 * (col // 3)
    for i in range(row_offset, 3+row_offset):
        for j in range(col_offset, 3+col_offset):
            if grille[i][j] == value:
                res = True
    return res

def resolver(grille):
    res = False # indication that one case as been resolved
    zeros = 0 # count remaining 0
    for i in range(9):
        for j in range (9):
            if grille[i][j] == 0:
                possibles = []
                for s in range(1,10):
                    if ((not find_in_row(grille, j, s)) and
                        (not find_in_col(grille, i, s)) and
                        (not find_in_square(grille, i, j, s))):
                        possibles.append(s)
                if len(possibles) == 1:
                    print("at place :", i, ",", j, " : value ", possibles[0])
                    grille[i][j] = possibles[0]
                    res = True
                else:
                    print("at place :", i, ",", j, " : values ", possibles)
                    zeros += 1
    if res: print ("ongoing ok")
    elif zeros > 0: print("blocked")
    else: print("done")
    return res

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


def afficher_grille_tkinter(grille):
    
    # Creation de la fenetre principale
    root = tk.Tk()
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

    # Lancer la boucle principale de Tkinter
    root.mainloop()

# Exemple de grille de Sudoku (0 represente une case vide)

grille_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_hard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 3, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0]
]

"""
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]
"""

easy = [
    [5, 0, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 0, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]  # La case manquante est ici, elle devrait etre 2
]

# Afficher la grille
#grille_sudoku = saisir_grille()
print("Grille saisie :")
for ligne in sudoku_hard:
    print(ligne)
#afficher_grille_tkinter(grille_sudoku)

iteration = 0
while resolver(sudoku_hard) and iteration < 10:
    iteration += 1
    print("Grille after ", iteration, " iteration(s)")
    for ligne in sudoku_hard:
        print(ligne)