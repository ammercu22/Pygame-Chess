class Player:
    def __init__(self, piecesColor):
        self.pieces = []
        self.opponentPieces = []
        self.piecesColor = piecesColor
        self.score = 0

    def set_pieces(self, updatedPieces):
        self.pieces = updatedPieces

    def set_score(self, updatedScore):
        self.score = updatedScore

    def get_pieces(self):
        return self.pieces
    
    def get_score(self):
        return self.score

    def add_opponent_piece(self, takenPiece):
        self.opponentPieces.append(takenPiece)
        self.score += takenPiece.pointVal
    
    def remove_piece(self, takenPiece):
        self.pieces.remove(takenPiece)

