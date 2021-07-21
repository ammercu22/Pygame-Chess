import pygame
import os
from constants import *
from board import *
pygame.display.set_caption("Chess")

def draw_window():
    #draw window prob where the board will be called
    wSpaces, bSpaces = draw_board()
    wPieces, bPieces = initBoard()
    for space in wSpaces:
        pygame.draw.rect(WIN, WHITE, space)
    for space in bSpaces:
        pygame.draw.rect(WIN, BLACK, space)

    for piece in bPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    for piece in wPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    
    pygame.display.update()

#def determine_square_pos():
    
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

        draw_window()

if __name__ == "__main__":
    main()