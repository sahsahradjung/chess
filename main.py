import chess
import pygame

board = chess.Board()
Square = 60
BOard = Square*8
pygame.init()
screen = pygame.display.set_mode((BOard, BOard))
pygame.display.set_caption("chess")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for row in range(8):
            for col in range(8):
                color = (189, 183, 137) if (row + col) % 2 == 0 else (112,86,50)
                pygame.draw.rect(screen, color, (col * Square, row * Square, Square, Square))
    pygame.display.flip()
pygame.quit()