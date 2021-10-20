import pygame
from piece import *
from constants import *

whitePieces = []
blackPieces = []

whiteSpaces = []
blackSpaces = []

flag = 0
#a function that returns two lists of all "space" objects on the board. 
def draw_board():
    currX = 0
    currY = 0
    flag = 0
    wSpaces = []
    bSpaces = []
    global whiteSpaces
    global blackSpaces

    #a nested while loop that calculates the x and y positions of each space, creates new "space" objects once the (x,y) coordinates are calculated, and appends each object to either
    #the 'wSpaces' list or 'bSpaces' list
    while currX <= 800:
        while currY <= 800:
            if flag == 0: #0 = white spaces
                space = pygame.Rect(currX, currY, BOARD_SPACE_WIDTH, BOARD_SPACE_HEIGHT)
                wSpaces.append(space)
                flag = 1
            elif flag == 1: # 1 = black spaces
                space = pygame.Rect(currX, currY, BOARD_SPACE_WIDTH, BOARD_SPACE_HEIGHT)
                bSpaces.append(space)
                flag = 0
            currY += 100
        currX += 100
        currY = 0
    whiteSpaces = wSpaces
    blackSpaces = bSpaces
    return (wSpaces, bSpaces)

#a function that returns 2 lists of all "pieces" objects that will be on the board.
def init_board():
    numPawns = 0
    bPieces = []
    wPieces = []
    global whitePieces
    global blackPieces
    #Black Pawn Locations
    currSpaceX = 0
    currSpaceY = 100
    currX = 25
    currY = 125
    #a while loop that calculates the (x,y) coordinates of all black pawns on the board, creates a pawn object once the coordinates are calculated, and adds the new pawn to the "bPieces" list
    while numPawns < 8:
        pawn = pygame.Rect(currX, currY, PIECE_WIDTH, PIECE_HEIGHT)
        newPiece = Piece("Pawn", "b", B_PAWN, pawn, currSpaceX, currSpaceX + 100, currSpaceY, currSpaceY + 100, 1)
        bPieces.append(newPiece)
        numPawns += 1
        currX += 100
        currSpaceX += 100

    leftRook = pygame.Rect(B_LEFT_ROOK_X, B_LEFT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftKnight = pygame.Rect(B_LEFT_KNIGHT_X, B_LEFT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftBishop = pygame.Rect(B_LEFT_BISHOP_X, B_LEFT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    queen = pygame.Rect(B_QUEEN_X, B_QUEEN_Y, PIECE_WIDTH, PIECE_HEIGHT)
    king = pygame.Rect(B_KING_X, B_KING_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightRook = pygame.Rect(B_RIGHT_ROOK_X, B_RIGHT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightKnight = pygame.Rect(B_RIGHT_KNIGHT_X, B_RIGHT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightBishop = pygame.Rect(B_RIGHT_BISHOP_X, B_RIGHT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    
    currSpaceX = 0
    currSpaceY = 0

    #Appends all other created pieces other than pawns to the "bPieces" list with their specific coordinates
    bPieces.append(Piece("Rook","b", B_ROOK, leftRook, currSpaceX, currSpaceX + 100, currSpaceY, currSpaceY + 100, 5))
    bPieces.append(Piece("Knight","b", B_KNIGHT, leftKnight, currSpaceX + 100, currSpaceX + 200, currSpaceY, currSpaceY + 100, 3))
    bPieces.append(Piece("Bishop","b", B_BISHOP, leftBishop, currSpaceX + 200, currSpaceX + 300, currSpaceY, currSpaceY + 100, 3))
    bPieces.append(Piece("Queen","b", B_QUEEN, queen, currSpaceX + 300, currSpaceX + 400, currSpaceY, currSpaceY + 100, 9))
    bPieces.append(Piece("King","b", B_KING, king, currSpaceX + 400, currSpaceX + 500, currSpaceY, currSpaceY + 100, 0))
    bPieces.append(Piece("Bishop","b", B_BISHOP, rightBishop, currSpaceX + 500, currSpaceX + 600, currSpaceY, currSpaceY + 100, 3))
    bPieces.append(Piece("Knight","b", B_KNIGHT, rightKnight, currSpaceX + 600, currSpaceX + 700, currSpaceY, currSpaceY + 100, 3))
    bPieces.append(Piece("Rook","b", B_ROOK, rightRook, currSpaceX + 700, currSpaceX + 800, currSpaceY, currSpaceY + 100, 5))

    
    numPawns = 0

    #White Pawn Locations
    currSpaceX = 0
    currSpaceY = 600
    currX = 25
    currY = 625
    #a while loop that calculates the (x,y) coordinates of all white pawns on the board, creates a pawn object once the coordinates are calculated, and adds the new pawn to the "wPieces" list
    while numPawns < 8:
        pawn = pygame.Rect(currX, currY, PIECE_WIDTH, PIECE_HEIGHT)
        newPiece = Piece("Pawn", "w", W_PAWN, pawn, currSpaceX, currSpaceX + 100, currSpaceY, currSpaceY + 100, 1)
        wPieces.append(newPiece)
        numPawns += 1
        currX += 100
        currSpaceX += 100

    leftRook = pygame.Rect(W_LEFT_ROOK_X, W_LEFT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftKnight = pygame.Rect(W_LEFT_KNIGHT_X, W_LEFT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftBishop = pygame.Rect(W_LEFT_BISHOP_X, W_LEFT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    queen = pygame.Rect(W_QUEEN_X, W_QUEEN_Y, PIECE_WIDTH, PIECE_HEIGHT)
    king = pygame.Rect(W_KING_X, W_KING_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightRook = pygame.Rect(W_RIGHT_ROOK_X, W_RIGHT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightKnight = pygame.Rect(W_RIGHT_KNIGHT_X, W_RIGHT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightBishop = pygame.Rect(W_RIGHT_BISHOP_X, W_RIGHT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    
    currSpaceX = 0
    currSpaceY = 700
    #Appends all other created pieces other than pawns to the "wPieces" list with their specific coordinates
    wPieces.append(Piece("Rook", "w", W_ROOK, leftRook, currSpaceX, currSpaceX + 100, currSpaceY, currSpaceY + 100, 5))
    wPieces.append(Piece("Knight","w", W_KNIGHT, leftKnight, currSpaceX + 100, currSpaceX + 200, currSpaceY, currSpaceY + 100, 3))
    wPieces.append(Piece("Bishop","w", W_BISHOP, leftBishop, currSpaceX + 200, currSpaceX + 300, currSpaceY, currSpaceY + 100, 3))
    wPieces.append(Piece("Queen","w", W_QUEEN, queen, currSpaceX + 300, currSpaceX + 400, currSpaceY, currSpaceY + 100, 9))
    wPieces.append(Piece("King","w", W_KING, king, currSpaceX + 400, currSpaceX + 500, currSpaceY, currSpaceY + 100, 0))
    wPieces.append(Piece("Bishop","w", W_BISHOP, rightBishop, currSpaceX + 500, currSpaceX + 600, currSpaceY, currSpaceY + 100, 3))
    wPieces.append(Piece("Knight","w", W_KNIGHT, rightKnight, currSpaceX + 600, currSpaceX + 700, currSpaceY, currSpaceY + 100, 3))
    wPieces.append(Piece("Rook","w", W_ROOK, rightRook, currSpaceX + 700, currSpaceX + 800, currSpaceY, currSpaceY + 100, 5))


   
    whitePieces = wPieces
    blackPieces = bPieces

    return (wPieces, bPieces)
    
def get_pieces():
    wPieces, bPieces = whitePieces, blackPieces
    return (wPieces, bPieces)

#checks to see if a piece exist where the player clicked on. If so, change piece position or do nothing
def check_space(mousePos): 
    global blackPieces
    global whitePieces
    selectedPiece = None
    for piece in blackPieces:
        if mousePos[0] > piece.spaceXLeftBound and mousePos[0] < piece.spaceXRightBound and mousePos[1] > piece.spaceYUpperBound and mousePos[1] < piece.spaceYLowerBound:
            selectedPiece = piece
            break
    for piece in whitePieces:
        if mousePos[0] > piece.spaceXLeftBound and mousePos[0] < piece.spaceXRightBound and mousePos[1] > piece.spaceYUpperBound and mousePos[1] < piece.spaceYLowerBound:
            selectedPiece = piece
            break
    return selectedPiece

#return true or false based on if the player's move was valid or not
def move_piece(mousePos, piece, playerPieces, opponentPieces):
    global blackSpaces
    global whiteSpaces
    retrictedMove = piece.move(mousePos, whiteSpaces, blackSpaces, playerPieces, opponentPieces)
    return retrictedMove