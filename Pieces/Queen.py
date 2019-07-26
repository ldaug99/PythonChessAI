class Queen:
    __type = "Queen"
    __color = ""
    __character = {"white": "♕", "black": "♛"}
    __image = {"white": "white_king.png", "black": "black_king.png"}

    def __init__(self, color):
        self.__color = color

    def getColor(self): return self.__color

    def getType(self): return self.__type
                
    def getCharacter(self): return self.__character

    def getImage(self): return self.__image