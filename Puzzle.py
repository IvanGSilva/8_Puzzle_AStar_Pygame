import random

# cria o tabuleiro com o estado desejado e o estado inicial é randomizado através da função shuffle()
class Puzzle:
    def __init__(self):
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.state = self.goal_state[:]
        self.shuffle()

    # função de embaralhar o tabuleiro
    # só deixa o tabuleiro ser exibido se ele tiver resolução, isso é possível pela função is_solvable()
    def shuffle(self):
        while True:
            random.shuffle(self.state)
            if self.is_solvable():
                break

    # por uma propriedade especial dos 8 puzzles, é possível saber se um tabuleiro tem resolução antes 
    # mesmo de tentar a resolução
    def is_solvable(self):
        inversions = sum(
            # o algoritmo faz inversões de pares até que todos os números estejam na ordem certa, se o número de 
            # inversões final for par, o tabuleiro tem resolução, caso não, o tabuleiro não tem resolução
            1 for i in range(len(self.state)) for j in range(i + 1, len(self.state))
            # o algoritmo ignora o quadrado com 0 (espaço vazio)
            if self.state[i] > self.state[j] != 0
        )
        return inversions % 2 == 0

    # função de mover os quadrados para o espaço com 0 (espaço vazio)
    def move(self, tile):
        zero_index = self.state.index(0)
        tile_index = self.state.index(tile)
        if tile_index in self.get_valid_moves(zero_index):
            self.state[zero_index], self.state[tile_index] = self.state[tile_index], self.state[zero_index]

    # define os movimentos válidos a partir da posição da peça 0
    def get_valid_moves(self, zero_index):
        row, col = divmod(zero_index, 3)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid = []
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                valid.append(new_row * 3 + new_col)
        return valid
