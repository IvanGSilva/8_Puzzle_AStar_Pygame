import pygame
# utilizado para "copiar" o estado inicial do tabuleiro para todas as heurísticas resolverem o mesmo estado inicial
from copy import deepcopy  
from Puzzle import Puzzle
from AStar import a_star
from Heuristics import manhattan_distance, inversion_pairs, misplaced_tiles
from UI import draw_buttons, draw_puzzle, draw_results, buttons, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

pygame.init()

# configurações de tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("8 Puzzle Solver")
font = pygame.font.Font(None, 36)

# função de animar os movimentos
def animate_moves(screen, font, puzzle, moves, delay=300):
    for move in moves:
        puzzle.state = move
        draw_puzzle(screen, font, puzzle)
        pygame.display.flip()
        pygame.time.delay(delay)

def main():
    puzzle = Puzzle()
    running = True
    solving = False
    solved = False
    results = {}
    heuristic_steps = {}
    heuristics = {
        "Manhattan": manhattan_distance,
        "Inversão": inversion_pairs,
        "Fora do lugar": misplaced_tiles
    }
    current_heuristic = None
    initial_state = None

    while running:
        # Lida com eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if buttons["shuffle"].collidepoint(mouse_pos):  # Botão de reembaralhar
                    puzzle.shuffle()
                    solving = False
                    solved = False
                    results = {}
                    heuristic_steps = {}
                elif buttons["solve"].collidepoint(mouse_pos):  # Botão de resolver
                    initial_state = deepcopy(puzzle.state)
                    solving = True
                    solved = False
                    results = {}
                    heuristic_steps = {}

        # Processa resolução, se necessário
        if solving and initial_state:
            for name, heuristic in heuristics.items():
                puzzle.state = deepcopy(initial_state)  # Restaura o estado inicial
                path, visited_count = a_star(puzzle.state, puzzle.goal_state, heuristic)
                results[name] = (len(path), visited_count)
                heuristic_steps[name] = path
                animate_moves(screen, font, puzzle, path)
            solving = False
            solved = True

        # Desenha a interface
        screen.fill(WHITE)  # Limpa a tela com a cor de fundo
        draw_puzzle(screen, font, puzzle)  # Desenha o tabuleiro
        draw_buttons(screen, font)  # Desenha os botões

        if solved and results:  # Exibe resultados se o puzzle foi resolvido
            draw_results(screen, font, results)

        # Atualiza a tela
        pygame.display.flip()

main()
pygame.quit()

