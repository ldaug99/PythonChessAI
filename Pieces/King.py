from Pieces.Piece import Piece

class King(Piece):
    __type = "King"
    __move = [(1,0),(0,1)]
    __character = {"white": "u2654", "black": "u265a"} # Unicode for ♔ and ♚
    __image = {"white": "white_king.png", "black": "black_king.png"}

    def __init__(self, color): 
        super().__init__(self.__type, color, self.__move, self.__character, self.__image)

    def getMoves(self, position):
        pass
