import pygame
import os
import main
from piece import *
from constants import *

def draw_board():
    currX = 0
    currY = 0
    flag = 0
    wSpaces = []
    bSpaces = []
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
    return (wSpaces, bSpaces)

def initBoard():
    numPawns = 0
    bPieces = []
    wPieces = []

    #Black Pawn Locations
    currX = 25
    currY = 125
    while numPawns < 8:
        pawn = pygame.Rect(currX, currY, PIECE_WIDTH, PIECE_HEIGHT)
        newPiece = Piece(B_PAWN, pawn)
        bPieces.append(newPiece)
        numPawns += 1
        currX += 100

    #Rest of black pieces
    leftRook = pygame.Rect(B_LEFT_ROOK_X, B_LEFT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftKnight = pygame.Rect(B_LEFT_KNIGHT_X, B_LEFT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftBishop = pygame.Rect(B_LEFT_BISHOP_X, B_LEFT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    queen = pygame.Rect(B_QUEEN_X, B_QUEEN_Y, PIECE_WIDTH, PIECE_HEIGHT)
    king = pygame.Rect(B_KING_X, B_KING_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightRook = pygame.Rect(B_RIGHT_ROOK_X, B_RIGHT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightKnight = pygame.Rect(B_RIGHT_KNIGHT_X, B_RIGHT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightBishop = pygame.Rect(B_RIGHT_BISHOP_X, B_RIGHT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    
    bPieces.append(Piece(B_ROOK, leftRook))
    bPieces.append(Piece(B_KNIGHT, leftKnight))
    bPieces.append(Piece(B_BISHOP, leftBishop))
    bPieces.append(Piece(B_QUEEN, queen))
    bPieces.append(Piece(B_KING, king))
    bPieces.append(Piece(B_ROOK, rightRook))
    bPieces.append(Piece(B_KNIGHT, rightKnight))
    bPieces.append(Piece(B_BISHOP, rightBishop))

    #White Pawn Locations
    numPawns = 0
    currX = 25
    currY = 625
    while numPawns < 8:
        pawn = pygame.Rect(currX, currY, PIECE_WIDTH, PIECE_HEIGHT)
        newPiece = Piece(W_PAWN, pawn)
        wPieces.append(newPiece)
        numPawns += 1
        currX += 100
    
    leftRook = pygame.Rect(W_LEFT_ROOK_X, W_LEFT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftKnight = pygame.Rect(W_LEFT_KNIGHT_X, W_LEFT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    leftBishop = pygame.Rect(W_LEFT_BISHOP_X, W_LEFT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    queen = pygame.Rect(W_QUEEN_X, W_QUEEN_Y, PIECE_WIDTH, PIECE_HEIGHT)
    king = pygame.Rect(W_KING_X, W_KING_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightRook = pygame.Rect(W_RIGHT_ROOK_X, W_RIGHT_ROOK_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightKnight = pygame.Rect(W_RIGHT_KNIGHT_X, W_RIGHT_KNIGHT_Y, PIECE_WIDTH, PIECE_HEIGHT)
    rightBishop = pygame.Rect(W_RIGHT_BISHOP_X, W_RIGHT_BISHOP_Y, PIECE_WIDTH, PIECE_HEIGHT)
    
    wPieces.append(Piece(W_ROOK, leftRook))
    wPieces.append(Piece(W_KNIGHT, leftKnight))
    wPieces.append(Piece(W_BISHOP, leftBishop))
    wPieces.append(Piece(W_QUEEN, queen))
    wPieces.append(Piece(W_KING, king))
    wPieces.append(Piece(W_ROOK, rightRook))
    wPieces.append(Piece(W_KNIGHT, rightKnight))
    wPieces.append(Piece(W_BISHOP, rightBishop))

    return (wPieces, bPieces)
    


