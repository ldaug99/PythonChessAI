class Piece:
    __type = ""
    __color = ""
    __move = []
    __character = {}
    __image = {}

    def __init__(self, _type, color, move, character, image):
        self.__type = _type
        self.__color = color
        self.__move = move
        self.__character = character
        self.__image = image                  

    def getColor(self): return self.__color

    def getType(self): return self.__type
                
    def getCharacter(self): return self.__character

    def getImage(self): 
        """self.__image"""
        return {"white": "white_king.png", "black": "black_king.png"}

    def getMoves(self, position):
        raise NotImplementedError("Must override getMoves")