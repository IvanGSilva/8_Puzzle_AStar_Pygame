import pygame
import textwrap

pygame.init()
pygame.font.init()

# configurações de UI
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

BUTTON_WIDTH, BUTTON_HEIGHT = 180, 50
# centraliza o tabuleiro na horizontal
PUZZLE_OFFSET_X = 100
# centraliza o tabuleiro na vertical
PUZZLE_OFFSET_Y = 50

# configurações dos botões
buttons = {
    "shuffle": pygame.Rect((SCREEN_WIDTH // 4) - (BUTTON_WIDTH // 2), 450, BUTTON_WIDTH, BUTTON_HEIGHT),
    "solve": pygame.Rect((3 * SCREEN_WIDTH // 4) - (BUTTON_WIDTH // 2), 450, BUTTON_WIDTH, BUTTON_HEIGHT)
}

body_font = pygame.font.Font(None, 24)

# cria os botões na tela
def draw_buttons(screen, font):
    pygame.draw.rect(screen, BLUE, buttons["shuffle"])
    shuffle_text = font.render("Reembaralhar", True, WHITE)
    screen.blit(shuffle_text, (buttons["shuffle"].centerx - shuffle_text.get_width() // 2, 
                               buttons["shuffle"].centery - shuffle_text.get_height() // 2))
    
    pygame.draw.rect(screen, GREEN, buttons["solve"])
    solve_text = font.render("Resolver", True, WHITE)
    screen.blit(solve_text, (buttons["solve"].centerx - solve_text.get_width() // 2, 
                             buttons["solve"].centery - solve_text.get_height() // 2))

# cria o tabuleiro na tela
def draw_puzzle(screen, font, puzzle):
    screen.fill(WHITE)
    for i, tile in enumerate(puzzle.state):
        x = PUZZLE_OFFSET_X + (i % 3) * 100
        y = PUZZLE_OFFSET_Y + (i // 3) * 100
        if tile != 0:
            pygame.draw.rect(screen, GRAY, (x, y, 100, 100))
            text = font.render(str(tile), True, BLACK)
            screen.blit(text, (x + 40, y + 30))
        else:
            pygame.draw.rect(screen, WHITE, (x, y, 100, 100))
        pygame.draw.rect(screen, BLACK, (x, y, 100, 100), 2)

# cria o relatório de resultados
def draw_results(screen, font, results):
    y_offset = 520  
    line_spacing = 30
    result_text = font.render("Resultados:", True, BLACK)
    screen.blit(result_text, (20, y_offset))
    
    # Renderiza cada resultado
    for i, (heuristic, (moves, visited)) in enumerate(results.items()):
        # Prepara o texto
        text = f"{heuristic}: {moves} movimentos, {visited} estados"
        
        # Divide o texto em linhas para caber na tela
        wrapped_text = textwrap.wrap(text, width=40)
        
        for j, line in enumerate(wrapped_text):
            rendered_line = body_font.render(line, True, BLACK) 
            screen.blit(rendered_line, (20, y_offset + line_spacing * (i + j + 1)))