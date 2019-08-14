from Pieces.Piece import Piece

class Queen(Piece):
    __type = "Queen"
    __move = []
    __character = {"white": "♕", "black": "♛"}
    __image = {"white": "white_queen.png", "black": "black_queen.png"}
    
    def __init__(self, color): 
        super().__init__(self.__type, color, self.__move, self.__character, self.__image)

    def getMoves(self, position):
        pass