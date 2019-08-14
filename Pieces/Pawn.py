from Pieces.Piece import Piece

class Pawn(Piece):
    __type = "Pawn"
    __move = []
    __direction = 1
    __character = {"white": "♙", "black": "♟"}
    __image = {"white": "white_pawn.png", "black": "black_pawn.png"}
    
    def __init__(self, color): 
        if (color == "black"):
            __direction = (-1)
        super().__init__(self.__type, color, self.__move, self.__character, self.__image)

    def getMoves(self, position):
        moves = []
        pass