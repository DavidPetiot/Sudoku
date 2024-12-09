import Samples
import sudoku as solver

# Afficher la grille
#grille = saisir_grille()
grille = Samples.sudoku_medium
print("Grille saisie :")
for ligne in grille:
    print(ligne)
#afficher_grille_tkinter(grille_sudoku)

iteration = 0
while solver.resolver(grille) and iteration < 10:
    iteration += 1
    print("Grille after ", iteration, " iteration(s)")
    for ligne in grille:
        print(ligne)