class Pawn:
    __name = "Pawn"
    __color = ""
    __position = [0,0]
    __direction = 1
    __character = {"white": "♙", "black": "♟"}
    
    def __init__(self, color, position):
        self.__color = color
        self.__position = position
        if (self.__color == "black"):
            __direction = (-1)

    def getColor(self): return self.__color

    def getName(self): return self.__name

    def getPosition(self): return self.__position

    def getCharacter(self): return self.__character