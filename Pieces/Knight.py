class Knight:
    __type = "Knight"
    __color = ""
    __movePattern = [(2,1)]
    __character = {"white": "♘", "black": "♞"}
    
    def __init__(self, color):
        self.__color = color

    def getColor(self): return self.__color

    def getType(self): return self.__type
        
    def getCharacter(self): return self.__character

    def getMoves(self, position):
        moves = []
        for i in range(0,len(self.__movePattern)):
            pattern = self.__movePattern[i]
            for k in range(-1,2,2):
                for h in range(-1,2,2):
                    _rank = position[0]+(pattern[0]*k)
                    _file = position[1]+(pattern[1]*h)
                    if _rank < 0 or _rank > 7 or _file < 0 or _file > 7:
                        continue
                    move = (_rank,_file)
                    moves.append(move)
        return moves