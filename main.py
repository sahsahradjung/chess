import chess
import pygame

board = chess.Board()
Square = 60
BOard = Square*8
pygame.init()
screen = pygame.display.set_mode((BOard, BOard))
pygame.display.set_caption("chess")
def squaR_r(pos):
    col = pos[0]//Square
    row = pos[1]//Square
    return chess.square_name(chess.square(col, 7-row))
def squa(sq_name):
    sq = chess.parse_square(sq_name)
    col = chess.square_file(sq)
    row = 7 - chess.square_rank(sq)
    return col*Square, row*Square
running = True
selected = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            sq_name = squaR_r(event.pos)
            print(f"Clicked {sq_name}")
            if selected is None:
                piece = board.piece_at(chess.parse_square(sq_name))
                if piece and piece.color == board.turn:
                    selected = sq_name
            else:
                move = chess.Move.from_uci(selected+sq_name)
                if move in board.legal_moves:
                    board.push(move)
                    print(f"Moved {board.pop() is None and move.uci()}")
                    board.push(move)
                    selected = None
        for row in range(8):
            for col in range(8):
                color = (189, 183, 137) if (row + col) % 2 == 0 else (112,86,50)
                pygame.draw.rect(screen, color, (col * Square, row * Square, Square, Square))  
    pygame.display.flip()

pygame.quit()