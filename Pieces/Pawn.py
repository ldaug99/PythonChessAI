class Pawn:
    __name = "Pawn"
    __color = ""

    __direction = 1
    __character = {"white": "♙", "black": "♟"}
    
    def __init__(self, color):
        self.__color = color
        if (self.__color == "black"):
            __direction = (-1)

    def getColor(self): return self.__color

    def getName(self): return self.__name

    def getCharacter(self): return self.__character