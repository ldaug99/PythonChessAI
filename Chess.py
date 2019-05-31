from appJar import gui

from Pieces.Pawn import Pawn as Pawn
from Pieces.Knight import Knight as Knight
from Pieces.Bishop import Bishop as Bishop
from Pieces.Rook import Rook as Rook
from Pieces.Queen import Queen as Queen
from Pieces.King import King as King

class Chess:
    app = gui("Chess", "600x600")
    __highlightColor = "LawnGreen"

    __pawn = 0
    __knight = 1
    __bishop = 2
    __rook = 3
    __queen = 4
    __king = 5

    def __init__(self):
        self.__chessboard = {}
        self.__white = "white"
        self.__black = "black"
        self.__noneChessboard()
        self.__setupChessboard()

    def __setupChessboard(self):
        lineup = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        for i in range(0,8):
            self.__chessboard[1,i] = Pawn(self.__black,[1,i])
            self.__chessboard[6,i] = Pawn(self.__white,[6,i])
            self.__chessboard[0,i] = lineup[i](self.__black,[0,i])
            self.__chessboard[7,i] = lineup[i](self.__white,[7,i])    

    def __noneChessboard(self):
        for i in range(0,8):
            for k in range (0,8):
                self.__chessboard[i,k] = None
    
    def getBoard(self):
        return self.__chessboard
    
    def getKeys(self):
        return list(self.__chessboard.keys())

    def getKeyFromPiece(self, piece):
        keys = self.getKeys()
        for i in range(len(keys)):
            if piece == self.__chessboard[keys[i]]:
                return keys[i]
        return None

    def getKeysForAllPieces(self):
        pieceKeys = []
        keys = self.getKeys()
        for i in range(len(keys)):
            if self.__chessboard[keys[i]] != None:
                pieceKeys.append(keys[i])
        return pieceKeys
    
    def movePieceByKey(self, fromKey, toKey):
        # Check if there is a piece at position
        # Check if piece can move in the selected pattern
        # Check if piece was taken
        self.__chessboard[toKey] = self.__chessboard[fromKey]
        self.__chessboard[fromKey] = None
        # Check if checkmate

    def getKeyByMatrix(self, rank, file):
        # rank is row, file is column as with matrices
        return [rank, file]
    
    def setupGUI(self):
        self.app.setSticky("news")
        self.app.setExpand("both")
        self.app.setFont(20)
        for i in range(0,8):
            for k in range(0,8):
                key = (i,k)
                label = str(i) + str(k)
                self.app.addLabel(label, self.getPieceCharacter(key), i, k)
                self.app.setLabelBg(label, self.getTileColor(key))
                self.app.setLabelFg(label, self.getPieceColor(key))
                self.makeClickable(label)
        self.app.go()

    def getPieceCharacter(self, key):
        if self.__chessboard[key] != None:
            pieceColor = self.__chessboard[key].getColor()
            return str(self.__chessboard[key].getCharacter()[pieceColor])
        else:
            return ""

    def getTileColor(self, key):
        if key[0]%2 == 0 and key[1]%2 == 0:
            return self.__white
        elif key[0]%2 == 1 and key[1]%2 == 0:
            return self.__black
        elif key[0]%2 == 0 and key[1]%2 == 1:
            return self.__black
        else:
            return self.__white
    
    def getPieceColor(self, key):
        if self.getTileColor(key) == self.__black:
            return self.__white
        else:
            return self.__black

    def labelToKey(self, label):
        return (int(label[0]),int(label[1]))

    def makeClickable(self, label):
        if self.__chessboard[self.labelToKey(label)] != None:
            self.app.setLabelSubmitFunction(label, self.setPieceHighlight)
        
    def setPieceHighlight(self, label):
        print(self.labelToKey(label))
        if self.__chessboard[self.labelToKey(label)] != None:
            self.app.setLabelBg(label, self.__highlightColor)
            self.app.setLabelBg(label, self.__black)
            print("Noice")
        else:
            print("Not noice")

    #def removePieceHighlight(self, key):

def Game():
    chess = Chess()
    print(chess.getBoard())


Game()


#__chessboard[i,1] = Pawn("black",[i,1])
#__chessboard[i,6] = Pawn("white",[i,6])