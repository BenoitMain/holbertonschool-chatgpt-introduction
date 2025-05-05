#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Sélection aléatoire et unique de mines dans [0 ... width*height)
        self.mines = set(random.sample(range(width * height), mines))
        # Champ de jeu, initialement caché
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # Grille de booléens pour savoir quelles cases ont été révélées
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # En-têtes de colonnes
        print('   ' + ' '.join(f"{i:2}" for i in range(self.width)))
        for y in range(self.height):
            # En-tête de ligne
            print(f"{y:2} ", end='')
            for x in range(self.width):
                idx = y * self.width + x
                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        print(' *', end='')   # Affiche une mine
                    else:
                        cnt = self.count_mines_nearby(x, y)
                        # Affiche le nombre de mines voisines (ou espace s’il est nul)
                        print(f" {cnt if cnt > 0 else ' '}", end='')
                else:
                    print(' .', end='')       # Case non révélée
            print()

    def count_mines_nearby(self, x, y):
        """Compter les mines dans les 8 cases adjacentes."""
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_cell(self, x, y):
        """Révèle la case (x,y). Retourne False si c’est une mine."""
        idx = y * self.width + x
        if idx in self.mines:
            return False  # Mine touchée

        self.revealed[y][x] = True

        # Si aucune mine autour, on « inonde » les cases adjacentes
        if self.count_mines_nearby(x, y) == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and 0 <= ny < self.height
                        and not self.revealed[ny][nx]):
                        self.reveal_cell(nx, ny)
        return True

    def has_won(self):
        """Vérifie si toutes les cases non-mines ont été révélées."""
        total_cells = self.width * self.height
        safe_cells = total_cells - len(self.mines)
        # Compte le nombre de cases déjà révélées
        revealed_count = sum(
            1 for row in self.revealed for cell in row if cell
        )
        return revealed_count == safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not self.reveal_cell(x, y):
                    # Si mine touchée → affichage complet et fin de partie
                    self.print_board(reveal=True)
                    print("\n💥 Game Over ! Vous avez déclenché une mine.")
                    break

                # Après chaque révélation sûre, on vérifie la victoire
                if self.has_won():
                    self.print_board(reveal=True)
                    print("\n🎉 Félicitations ! Vous avez dégagé tout le champ.")
                    break

            except ValueError:
                print("Entrée invalide. Veuillez saisir des nombres uniquement.")
            except IndexError:
                print("Coordonnées hors limites. Réessayez.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
