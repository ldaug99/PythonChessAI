from Pieces.Piece import Piece

class Knight(Piece):
    __type = "Knight"
    __move = [(2,1)]
    __character = {"white": "♘", "black": "♞"}
    __image = {"white": "white_knight.png", "black": "black_knight.png"}
    
    def __init__(self, color): 
        super().__init__(self.__type, color, self.__move, self.__character, self.__image)

    def getMoves(self, position):
        moves = []
        for i in range(0,len(self.__move)):
            pattern = self.__move[i]
            for k in range(-1,2,2):
                for h in range(-1,2,2):
                    _rank = position[0]+(pattern[0]*k)
                    _file = position[1]+(pattern[1]*h)
                    if _rank < 0 or _rank > 7 or _file < 0 or _file > 7:
                        continue
                    move = (_rank,_file)
                    moves.append(move)
        return moves