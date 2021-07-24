import pygame
import os

class Piece:
    def __init__ (self, image, rect, spaceXLeftBound, spaceXRightBound, spaceYUpperBound, spaceYLowerBound ):
        self.image = image
        self.rect = rect
        self.spaceXLeftBound = spaceXLeftBound
        self.spaceXRightBound = spaceXRightBound
        self.spaceYUpperBound = spaceYUpperBound
        self.spaceYLowerBound = spaceYLowerBound 

    def move(self, mousePos, wSpaces, bSpaces):
        print(mousePos)
        for space in bSpaces:
            if mousePos[0] > space.x and mousePos[0] < space.x + 100 and mousePos[1] > space.y and mousePos[1] < space.y + 100:
                print(self.rect.x, self.rect.y)
                self.rect.x = space.x + 25
                self.rect.y = space.y + 25
                self.spaceXLeftBound = space.x
                self.spaceXRightBound = space.x + 100
                self.spaceYUpperBound= space.y
                self.spaceYLowerBound  = space.y + 100
                print(self.rect.x, self.rect.y)
                break
        for space in wSpaces:
            if mousePos[0] > space.x and mousePos[0] < space.x + 100 and mousePos[1] > space.y and mousePos[1] < space.y + 100:
                print(self.rect.x, self.rect.y)
                self.rect.x = space.x + 25
                self.rect.y = space.y + 25
                self.spaceXLeftBound = space.x
                self.spaceXRightBound = space.x + 100
                self.spaceYUpperBound= space.y
                self.spaceYLowerBound  = space.y + 100
                print(self.rect.x, self.rect.y)
                break

    
