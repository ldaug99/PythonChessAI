from Pieces.Piece import Piece

class Rook(Piece):
    __type = "Rook"
    __move = []
    __character = {"white": "♖", "black": "♜"}
    __image = {"white": "white_rook.png", "black": "black_rook.png"}
    
    def __init__(self, color): 
        super().__init__(self.__type, color, self.__move, self.__character, self.__image)

    def getMoves(self, position):
        pass