from Pieces.Piece import Piece

class Bishop(Piece):
    __type = "Bishop"
    __move = []
    __character = {"white": "♗", "black": "♝"}
    __image = {"white": "white_bishop.png", "black": "black_bishop.png"}
    
    def __init__(self, color): 
        super().__init__(self.__type, color, self.__move, self.__character, self.__image)

    def getMoves(self, position):
        pass