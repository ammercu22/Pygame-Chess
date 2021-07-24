import pygame
import os
from constants import *
from board import *
pygame.display.set_caption("Chess")


def draw_window(flag):
    #draw window prob where the board will be called
    wSpaces, bSpaces = draw_board()
    wPieces = [] 
    bPieces = []

   
    if flag == 0:
        wPieces, bPieces = init_board()
    else:
        wPieces, bPieces = get_pieces()

    for space in wSpaces:
        pygame.draw.rect(WIN, WHITE, space)
    for space in bSpaces:
        pygame.draw.rect(WIN, BLACK, space)

    for piece in bPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    for piece in wPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    
    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()
    flag = 0 
    piece = None
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if piece == None and event.type == pygame.MOUSEBUTTONDOWN:
                print("finding piece")
                mousePos = pygame.mouse.get_pos()
                piece = check_space(mousePos)
            elif piece != None and event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                move_piece(mousePos, piece)
                piece = None
        draw_window(flag)
        if flag == 0:
            flag = 1

if __name__ == "__main__":
    main()