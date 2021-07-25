class Piece:
    pawnMoved = 0
    def __init__ (self, name, color, image, rect, spaceXLeftBound, spaceXRightBound, spaceYUpperBound, spaceYLowerBound ):
        self.name = name
        self.color = color
        self.image = image
        self.rect = rect
        self.spaceXLeftBound = spaceXLeftBound
        self.spaceXRightBound = spaceXRightBound
        self.spaceYUpperBound = spaceYUpperBound
        self.spaceYLowerBound = spaceYLowerBound 


    def move(self, mousePos, wSpaces, bSpaces):
        for space in bSpaces:
            if mousePos[0] > space.x and mousePos[0] < space.x + 100 and mousePos[1] > space.y and mousePos[1] < space.y + 100:
                if self.check_restriction(space) == False:
                    #print(self.rect.x, self.rect.y)
                    self.rect.x = space.x + 25
                    self.rect.y = space.y + 25
                    self.spaceXLeftBound = space.x
                    self.spaceXRightBound = space.x + 100
                    self.spaceYUpperBound= space.y
                    self.spaceYLowerBound  = space.y + 100
                    #print(self.rect.x, self.rect.y)
                    break
        for space in wSpaces:
            if mousePos[0] > space.x and mousePos[0] < space.x + 100 and mousePos[1] > space.y and mousePos[1] < space.y + 100:
                if self.check_restriction(space) == False:
                    self.rect.x = space.x + 25
                    self.rect.y = space.y + 25
                    self.spaceXLeftBound = space.x
                    self.spaceXRightBound = space.x + 100
                    self.spaceYUpperBound= space.y
                    self.spaceYLowerBound  = space.y + 100
                    break
    def check_restriction(self, space):
        pieceCurrXPos = self.rect.x - 25
        pieceCurrYPos = self.rect.y - 25
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
                    if (pieceCurrYPos - space.y == -100 or pieceCurrYPos - space.y == -200) and pieceCurrXPos == space.x:
                        self.pawnMoved = 1
                        return False
                else:
                    if (pieceCurrYPos - space.y == 100 or pieceCurrYPos - space.y == 200) and pieceCurrXPos == space.x:
                        self.pawnMoved = 1
                        return False
            else:
                if self.color == "b":
                    if pieceCurrYPos - space.y == -100 and pieceCurrXPos == space.x:
                        return False
                else:
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


    
