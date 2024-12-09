import tkinter as tk
import Samples as samples
import sudoku as solver

class DataModel:
    """Modele de donnees avec gestion des observateurs."""
    def __init__(self):
        #self.data = [[0] * 9 for _ in range(9)] # all 0 by default
        self.data = samples.sudoku_medium
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer()

    def solve(self):
        solver.resolver(self.data)
        self.notify_observers()

class App:
    """Interface graphique qui se met a jour en fonction des modifications du modele."""
    def __init__(self, root, model):
        self.model = model
        self.root = root

        self.taille_case = 50
        self.taille_grille = self.taille_case * 9

        self.canevas = tk.Canvas(root, width=self.taille_grille, height=self.taille_grille, bg='white')
        self.canevas.pack()
        self.update_grid() #first display

        self.go_button = tk.Button(root, text="solve", command=self.run)
        self.go_button.pack()

        # S'abonner aux changements de donnees
        self.model.add_observer(self.update_grid)

    def run(self):
        self.model.solve()

    def update_grid(self):
        # Met a jour la grille avec les donnees actuelles
        self.canevas.delete("all")

        for i in range(10): #0-9
            # Epaissir les lignes pour les blocs 3x3
            epaisseur = 3 if i % 3 == 0 else 1

            # Lignes horizontales
            self.canevas.create_line(0, i * self.taille_case, self.taille_grille, i * self.taille_case, width=epaisseur)

            # Lignes verticales
            self.canevas.create_line(i * self.taille_case, 0, i * self.taille_case, self.taille_grille, width=epaisseur)

            # Ajouter les chiffres dans les cases
        for i in range(9):
            for j in range(9):
                if self.model.data[i][j] != 0:  # Si la case n'est pas vide
                    self.canevas.create_text(
                        j * self.taille_case + self.taille_case // 2,
                        i * self.taille_case + self.taille_case // 2,
                        text=str(self.model.data[i][j]),
                        font=("Helvetica", 16),
                        fill="black"
                    )

# Initialisation
if __name__ == "__main__":
    root = tk.Tk()
    root.title("IHM Dynamique")
    model = DataModel()
    app = App(root, model)
    root.mainloop()
