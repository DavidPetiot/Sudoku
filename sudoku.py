
import Cell as Cell
import Samples

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
                    print("at place :", i, j, " : value ", possibles[0])
                    grille[i][j] = possibles[0]
                    res = True
                else:
                    print("at place :", i, j, " : values ", possibles)
                    zeros += 1
    if res: print ("ongoing ok")
    elif zeros > 0: print("blocked")
    else: print("done")
    return res

# Afficher la grille
#grille = saisir_grille()
grille = Samples.sudoku_hard
print("Grille saisie :")
for ligne in grille:
    print(ligne)
#afficher_grille_tkinter(grille_sudoku)

iteration = 0
while resolver(grille) and iteration < 10:
    iteration += 1
    print("Grille after ", iteration, " iteration(s)")
    for ligne in grille:
        print(ligne)