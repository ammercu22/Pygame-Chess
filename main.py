import pygame
import os
from constants import *
from board import *
from player import *
pygame.display.set_caption("Chess")
pygame.font.init()

p1 = Player("w") 
p2 = Player("b")
def draw_window(flag, turn):
    #draw window prob where the board will be called
    global p1
    global p2
    playerFontWidth = None
    wSpaces, bSpaces = draw_board()
    wPieces = [] 
    bPieces = []
    
    WIN.fill(pygame.Color("black")) # erases the entire screen surface
    if flag == 0:
        wPieces, bPieces = init_board()
        p1.set_pieces(wPieces)
        p2.set_pieces(bPieces)
    else:
        wPieces, bPieces = get_pieces()
        p1.set_pieces(wPieces)
        p2.set_pieces(bPieces)

    for space in wSpaces:
        pygame.draw.rect(WIN, WHITE, space)
    for space in bSpaces:
        pygame.draw.rect(WIN, BLUE, space)

    for piece in bPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    for piece in wPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    
    w_score_text = GENERAL_FONT.render("Score: " + str(p1.get_score()), True, WHITE, BLACK)
    b_score_text = GENERAL_FONT.render("Score: " + str(p2.get_score()), True, WHITE, BLACK)

    if turn == 0:
        player_turn_text = GENERAL_FONT.render("Player 1's turn", True, WHITE, BLACK)
        playerFontWidth = 200
    else:
        player_turn_text = GENERAL_FONT.render("Player 2's turn", True, WHITE, BLACK)
        playerFontWidth = 400
    
    WIN.blit(w_score_text, (25,0))
    WIN.blit(b_score_text, (700,0))
    WIN.blit(player_turn_text, (playerFontWidth,0))

    pygame.display.update()



def main():
    global p1
    global p2
    run = True
    clock = pygame.time.Clock()
    flag = 0 
    piece = None
    turn = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if piece == None and event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                piece = check_space(mousePos)
            elif piece != None and event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if turn == 0:
                    restrictedMove = move_piece(mousePos, piece, p1, p2)
                    if restrictedMove == False:
                        turn = 1
                else:
                    restrictedMove = move_piece(mousePos, piece, p2, p1)
                    if restrictedMove == False:
                        turn = 0
                piece = None
        draw_window(flag, turn)
        if flag == 0:
            flag = 1

if __name__ == "__main__":
    main()