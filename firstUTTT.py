class UltimateTicTacToe:
    def __init__(self):
        # Initialisation du grand plateau et des petits tableaux
        self.board = [[[' ' for _ in range(3)] for _ in range(3)] for _ in range(9)]
        self.current_board = 0
        self.player = 'X'

    def print_board(self):
        # Affichage du plateau
        for row in range(3):
            for sub_row in range(3):
                for col in range(3):
                    print(' '.join(self.board[row * 3 + col][sub_row]), end=' | ')
                print()
            if row < 2:
                print('-' * 29)

    def check_winner(self, board):
        # Vérification des conditions de victoire sur un petit tableau
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] != ' ':
                return board[row][0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[1][1]
        return None

    def play_move(self, board, row, col):
        # Jouer un coup
        if self.board[board][row][col] == ' ':
            self.board[board][row][col] = self.player
            if self.check_winner(self.board[board]):
                print(f"Le joueur {self.player} a gagné le tableau {board}!")
            self.player = 'O' if self.player == 'X' else 'X'
            self.current_board = row * 3 + col
        else:
            print("Case déjà occupée, essayez à nouveau.")

    def start_game(self):
        # Démarrage du jeu
        while True:
            self.print_board()
            print(f"Joueur {self.player}, choisissez une ligne et une colonne pour jouer (tableau {self.current_board}):")
            row, col = map(int, input().split())
            self.play_move(self.current_board, row, col)

# Démarrer le jeu
game = UltimateTicTacToe()
game.start_game()
