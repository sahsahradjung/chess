import chess
import pygame
import chess.svg

board = chess.Board()
Square = 60
BOard = Square*8
pygame.init()
screen = pygame.display.set_mode((BOard, BOard))
pygame.display.set_caption("chess")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

        screen.fill("green")
        pygame.display.flip()
pygame.quit()