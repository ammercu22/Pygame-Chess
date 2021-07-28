
class Piece:
    pawnMoved = 0
    def __init__ (self, name, color, image, rect, spaceXLeftBound, spaceXRightBound, spaceYUpperBound, spaceYLowerBound, pointVal):
        self.name = name
        self.color = color
        self.image = image
        self.rect = rect
        self.spaceXLeftBound = spaceXLeftBound
        self.spaceXRightBound = spaceXRightBound
        self.spaceYUpperBound = spaceYUpperBound
        self.spaceYLowerBound = spaceYLowerBound
        self.pointVal = pointVal


    def move(self, mousePos, wSpaces, bSpaces, player, opponent):
        for space in bSpaces:
            if mousePos[0] > space.x and mousePos[0] < space.x + 100 and mousePos[1] > space.y and mousePos[1] < space.y + 100:
                if self.check_restriction(space, player, opponent) == False:
                    self.check_attack(space, player, opponent)
                    self.rect.x = space.x + 25
                    self.rect.y = space.y + 25
                    self.spaceXLeftBound = space.x
                    self.spaceXRightBound = space.x + 100
                    self.spaceYUpperBound= space.y
                    self.spaceYLowerBound  = space.y + 100
                    return False
        for space in wSpaces:
            if mousePos[0] > space.x and mousePos[0] < space.x + 100 and mousePos[1] > space.y and mousePos[1] < space.y + 100:
                if self.check_restriction(space, player, opponent) == False:
                    self.check_attack(space, player, opponent)
                    self.rect.x = space.x + 25
                    self.rect.y = space.y + 25
                    self.spaceXLeftBound = space.x
                    self.spaceXRightBound = space.x + 100
                    self.spaceYUpperBound= space.y
                    self.spaceYLowerBound  = space.y + 100
                    return False
        return True

    def check_restriction(self, space, player, opponent):
        pieceCurrXPos = self.rect.x - 25
        pieceCurrYPos = self.rect.y - 25
        if player.piecesColor == self.color:
            for piece in player.get_pieces():
                if piece.rect.x == space.x + 25 and piece.rect.y == space.y + 25:
                    return True
            if self.name == "Bishop":
                if abs(pieceCurrXPos - space.x) / 100 == abs(pieceCurrYPos - space.y) / 100:
                    return False
            if self.name == "Knight":
                if abs(pieceCurrXPos - space.x) == 100 and abs(pieceCurrYPos - space.y) == 200:
                    return False
                elif abs(pieceCurrXPos - space.x) == 200 and abs(pieceCurrYPos - space.y) == 100:
                    return False
            if self.name == "King":
                if abs(pieceCurrXPos - space.x) == 100 and pieceCurrYPos == space.y:
                    return False
                elif abs(pieceCurrYPos - space.y) == 100 and pieceCurrXPos == space.x:
                    return False
                elif abs(pieceCurrXPos - space.x) == 100 and abs(pieceCurrYPos - space.y) == 100:
                    return False
            if self.name == "Pawn":
                if self.pawnMoved == 0:
                    if self.color == "b":
                        for piece in opponent.get_pieces():
                            if piece.rect.x == self.rect.x and (piece.rect.y == self.rect.y + 100 or piece.rect.y == self.rect.y + 200):
                                return True
                        if (pieceCurrXPos - space.x == 100 or pieceCurrXPos - space.x == -100) and pieceCurrYPos - space.y == -100:
                            for piece in opponent.get_pieces():
                                if piece.rect.x == space.x + 25 and piece.rect.y == space.y + 25:
                                    return False
                        if (pieceCurrYPos - space.y == -100 or pieceCurrYPos - space.y == -200) and pieceCurrXPos == space.x:
                            self.pawnMoved = 1
                            return False
                    else:
                        for piece in opponent.get_pieces():
                            if piece.rect.x == self.rect.x and (piece.rect.y == self.rect.y - 100 or piece.rect.y == self.rect.y - 200):
                                return True
                        if (pieceCurrXPos - space.x == 100 or pieceCurrXPos - space.x == -100) and pieceCurrYPos - space.y == 100:
                            for piece in opponent.get_pieces():
                                if piece.rect.x == space.x + 25 and piece.rect.y == space.y + 25:
                                    return False
                        if (pieceCurrYPos - space.y == 100 or pieceCurrYPos - space.y == 200) and pieceCurrXPos == space.x:
                            self.pawnMoved = 1
                            return False
                else:
                    if self.color == "b":
                        for piece in opponent.get_pieces():
                            if piece.rect.x == self.rect.x and piece.rect.y == self.rect.y + 100:
                                return True
                        if (pieceCurrXPos - space.x == 100 or pieceCurrXPos - space.x == -100) and pieceCurrYPos - space.y == -100:
                            print (space.x + 25, space.y + 25)
                            for piece in opponent.get_pieces():
                                if piece.rect.x == space.x + 25 and piece.rect.y == space.y + 25:
                                    return False
                        if pieceCurrYPos - space.y == -100 and pieceCurrXPos == space.x:
                            return False
                    else:
                        for piece in opponent.get_pieces():
                            if piece.rect.x == self.rect.x and piece.rect.y == self.rect.y - 100:
                                return True
                        if (pieceCurrXPos - space.x == 100 or pieceCurrXPos - space.x == -100) and pieceCurrYPos - space.y == 100:
                            for piece in opponent.get_pieces():
                                print (piece.rect.x, piece.rect.y)
                                if piece.rect.x == space.x + 25 and piece.rect.y == space.y + 25:
                                    return False
                        if pieceCurrYPos - space.y == 100 and pieceCurrXPos == space.x:
                            return False
            if self.name == "Queen":
                if abs(pieceCurrXPos - space.x) / 100 == abs(pieceCurrYPos - space.y) / 100:
                    return False
                elif pieceCurrXPos != space.x and pieceCurrYPos == space.y:
                    return False
                elif pieceCurrXPos == space.x and pieceCurrYPos != space.y:
                    return False
            if self.name == "Rook":
                if pieceCurrXPos != space.x and pieceCurrYPos == space.y:
                    return False
                elif pieceCurrXPos == space.x and pieceCurrYPos != space.y:
                    return False
        return True
    
    def check_attack(self, space, player, opponent):
        for piece in opponent.get_pieces():
            if piece.rect.x == space.x + 25 and piece.rect.y == space.y + 25:
                self.take_piece(piece, player, opponent)

    def take_piece(self, takenPiece, player, opponent):
        opponent.remove_piece(takenPiece)
        player.add_opponent_piece(takenPiece)



    
