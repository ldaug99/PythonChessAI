class Bishop:
    __name = "Bishop"
    __color = ""
    __position = [0,0]
    __character = {"white": "♗", "black": "♝"}
    
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    def getColor(self): return self.__color

    def getName(self): return self.__name

    def getPosition(self): return self.__position
        
    def getCharacter(self): return self.__character