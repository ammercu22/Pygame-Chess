import pygame
import os
from constants import *
from board import *
from player import *
pygame.display.set_caption("Chess")
pygame.font.init()

p1 = Player("w") 
p2 = Player("b")
#Function that draws (displays) all pieces, spaces, and scores onto the board
def draw_window(flag, turn):
    global p1
    global p2
    playerFontWidth = None
    wSpaces, bSpaces = draw_board()
    wPieces = [] 
    bPieces = []
    
    WIN.fill(pygame.Color("black")) # erases all information from last turn on the board so previous info. isn't shown on current turn
    
    #if/else statement that checks if the game has just started or not. If the game has just started, set the position of the pieces to their initial setup. If not, set the position of
    #the pieces to their updated position(where they were moved to)
    if flag == 0:
        wPieces, bPieces = init_board()
        p1.set_pieces(wPieces)
        p2.set_pieces(bPieces)
    else:
        wPieces, bPieces = get_pieces()
        p1.set_pieces(wPieces)
        p2.set_pieces(bPieces)

    #Two "for" loops that draw the spaces onto the board
    for space in wSpaces:
        pygame.draw.rect(WIN, WHITE, space)
    for space in bSpaces:
        pygame.draw.rect(WIN, BLUE, space)

    #Two "for" loops that draw the pieces onto the board
    for piece in bPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    for piece in wPieces:
        WIN.blit(piece.image, (piece.rect.x, piece.rect.y))
    
    #setting variables to hold the rendered score of each player
    w_score_text = GENERAL_FONT.render("Score: " + str(p1.get_score()), True, WHITE, GRAY)
    b_score_text = GENERAL_FONT.render("Score: " + str(p2.get_score()), True, WHITE, GRAY)
    space_text = GENERAL_FONT.render("                                                                                                                                                  ", True, WHITE, GRAY)
    #setting variables to hold which player's turn it is in the game
    if turn == 0:
        player_turn_text = GENERAL_FONT.render("Player 1's turn", True, WHITE, GRAY)
        playerFontWidth = 200
    else:
        player_turn_text = GENERAL_FONT.render("Player 2's turn", True, WHITE, GRAY)
        playerFontWidth = 400
    

    #4 "blit" functions that display players' score and who's turn it is
    WIN.blit(space_text, (0,0))
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
            #if statement that checks if any player has quit out of the game. If the player did so, the game will stop running
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            #if no pieces were selected (piece == None) and a player has clicked down on their mouse, this means a player might want to select a piece.
            if piece == None and event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                #in order to check to see if the player clicked on a piece, check_space() is called. This function returns a piece if the space contains a piece. If no piece exists
                #on the space, the function returns None.
                piece = check_space(mousePos)
            #if a piece was selected (piece != None) and a player has clicked down on their mouse, this means a player is moving a piece to a different space
            elif piece != None and event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if turn == 0: #player 1's turn (white pieces)
                    #move_piece() checks to see if a player moves their piece to a valid space. It returns true or false based on if they do so.
                    restrictedMove = move_piece(mousePos, piece, p1, p2)
                    if restrictedMove == False:
                        turn = 1
                else: #player 2's turn (black pieces)
                    restrictedMove = move_piece(mousePos, piece, p2, p1)
                    #move_piece() checks to see if a player moves their piece to a valid space. It returns true or false based on if they do so.
                    if restrictedMove == False:
                        turn = 0
                piece = None
        draw_window(flag, turn)
        if flag == 0:
            flag = 1

if __name__ == "__main__":
    main()
