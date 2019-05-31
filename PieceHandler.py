from Pieces.Pawn import Pawn
from Pieces.King import King

class PieceHandler:
    def __init__(self, type, color, position):
        self.__color = color
        self.__position = position
        if (self.__color == "black"):
            __direction = (-1)
        self.pieceType(type)

    def pieceType(self, type):
        switcher = {
            0:Pawn,
            #1:spawnKnight,
            #2:spawnBishop,
            #3:spawnRook,
            #4:spawnQuenn,
            5:King
        }
        # Get the function from switcher dictionary
        action = switcher.get(type)
        # Execute the function
        return action(self.__color, self.__position)