import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 800, 900
BOARD_SPACE_WIDTH, BOARD_SPACE_HEIGHT = 100, 100
PIECE_WIDTH, PIECE_HEIGHT = 50, 50

WHITE = (255, 255, 255)
BLACK= (0,0,0)
BLUE = (102,153,255)

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

B_LEFT_ROOK_X, B_LEFT_ROOK_Y = 25, 125
B_LEFT_KNIGHT_X, B_LEFT_KNIGHT_Y = B_LEFT_ROOK_X + 100, B_LEFT_ROOK_Y 
B_LEFT_BISHOP_X, B_LEFT_BISHOP_Y = B_LEFT_ROOK_X+ 200, B_LEFT_ROOK_Y 
B_QUEEN_X, B_QUEEN_Y = B_LEFT_ROOK_X + 300, B_LEFT_ROOK_Y 
B_KING_X, B_KING_Y = B_LEFT_ROOK_X + 400, B_LEFT_ROOK_Y 
B_RIGHT_BISHOP_X, B_RIGHT_BISHOP_Y = B_LEFT_ROOK_X + 500, B_LEFT_ROOK_Y 
B_RIGHT_KNIGHT_X, B_RIGHT_KNIGHT_Y = B_LEFT_ROOK_X + 600, B_LEFT_ROOK_Y 
B_RIGHT_ROOK_X, B_RIGHT_ROOK_Y = B_LEFT_ROOK_X + 700, B_LEFT_ROOK_Y 

W_LEFT_ROOK_X, W_LEFT_ROOK_Y = 25, 825
W_LEFT_KNIGHT_X, W_LEFT_KNIGHT_Y = W_LEFT_ROOK_X + 100, W_LEFT_ROOK_Y 
W_LEFT_BISHOP_X, W_LEFT_BISHOP_Y = W_LEFT_ROOK_X+ 200, W_LEFT_ROOK_Y 
W_QUEEN_X, W_QUEEN_Y = W_LEFT_ROOK_X + 300, W_LEFT_ROOK_Y 
W_KING_X, W_KING_Y = W_LEFT_ROOK_X + 400, W_LEFT_ROOK_Y 
W_RIGHT_BISHOP_X, W_RIGHT_BISHOP_Y = W_LEFT_ROOK_X + 500, W_LEFT_ROOK_Y 
W_RIGHT_KNIGHT_X, W_RIGHT_KNIGHT_Y = W_LEFT_ROOK_X + 600, W_LEFT_ROOK_Y 
W_RIGHT_ROOK_X, W_RIGHT_ROOK_Y = W_LEFT_ROOK_X + 700, W_LEFT_ROOK_Y 

B_BISHOP_IMAGE = pygame.image.load(os.path.join('Assets', 'bB.png'))
B_KING_IMAGE = pygame.image.load(os.path.join('Assets', 'bK.png'))
B_KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'bN.png'))
B_PAWN_IMAGE = pygame.image.load(os.path.join('Assets', 'bp.png'))
B_QUEEN_IMAGE = pygame.image.load(os.path.join('Assets', 'bQ.png'))
B_ROOK_IMAGE = pygame.image.load(os.path.join('Assets', 'bR.png'))

B_BISHOP = pygame.transform.scale(B_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
B_KING = pygame.transform.scale(B_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
B_KNIGHT = pygame.transform.scale(B_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
B_PAWN = pygame.transform.scale(B_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
B_QUEEN = pygame.transform.scale(B_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
B_ROOK = pygame.transform.scale(B_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

W_BISHOP_IMAGE = pygame.image.load(os.path.join('Assets', 'wB.png'))
W_KING_IMAGE = pygame.image.load(os.path.join('Assets', 'wK.png'))
W_KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'wN.png'))
W_PAWN_IMAGE = pygame.image.load(os.path.join('Assets', 'wp.png'))
W_QUEEN_IMAGE = pygame.image.load(os.path.join('Assets', 'wQ.png'))
W_ROOK_IMAGE = pygame.image.load(os.path.join('Assets', 'wR.png'))

W_BISHOP = pygame.transform.scale(W_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
W_KING = pygame.transform.scale(W_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
W_KNIGHT = pygame.transform.scale(W_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
W_PAWN = pygame.transform.scale(W_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
W_QUEEN = pygame.transform.scale(W_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))
W_ROOK = pygame.transform.scale(W_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))


GENERAL_FONT = pygame.font.SysFont('comicsans', 30)
