class Queen:
    __name = "Queen"
    __color = ""
    __character = {"white": "♕", "black": "♛"}

    def __init__(self, color):
        self.__color = color

    def getColor(self): return self.__color

    def getName(self): return self.__name
                
    def getCharacter(self): return self.__character