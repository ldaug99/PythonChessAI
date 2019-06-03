from appJar import gui

class GUI:
    app = gui("Chess", "600x600")
    __highlightTile = "LawnGreen"
    __lightTile = "white"
    __darkTile = "black"
    __chessboard = {}

    def __init__(self, chessboard):
        self.app.setSticky("news")
        self.app.setExpand("both")
        self.app.setFont(20)
        self.updateGUI(chessboard)

    def updateGUI(self, chessboard):
        self.__chessboard = chessboard
        for i in range(0,8):
            for k in range(0,8):
                key = (i,k)
                label = str(i) + str(k)
                self.app.addLabel(label, self.getPieceCharacter(key), i, k)
                self.app.setLabelBg(label, self.getTileColor(key))
                self.app.setLabelFg(label, self.getPieceColor(key))
                self.makeClickable(label)
        self.app.go()

    def setTileColors(self, light, dark):
        self.__lightTile = light
        self.__darkTile = dark

    def getPieceCharacter(self, key):
        if self.__chessboard[key] != None:
            pieceColor = self.__chessboard[key].getColor()
            return str(self.__chessboard[key].getCharacter()[pieceColor])
        else:
            return ""

    def getTileColor(self, key):
        if key[0]%2 == 0 and key[1]%2 == 0:
            return self.__lightTile
        elif key[0]%2 == 1 and key[1]%2 == 0:
            return self.__darkTile
        elif key[0]%2 == 0 and key[1]%2 == 1:
            return self.__darkTile
        else:
            return self.__lightTile
    
    def getPieceColor(self, key):
        if self.getTileColor(key) == self.__darkTile:
            return self.__lightTile
        else:
            return self.__darkTile

    def labelToKey(self, label):
        return (int(label[0]),int(label[1]))

    def makeClickable(self, label):
        if self.__chessboard[self.labelToKey(label)] != None:
            self.app.setLabelSubmitFunction(label, self.setPieceHighlight)
        
    def setPieceHighlight(self, label):
        print(self.labelToKey(label))
        if self.__chessboard[self.labelToKey(label)] != None:
            self.app.setLabelBg(label, self.__highlightTile)
            self.app.setLabelFg(label, self.__darkTile)
            print("Noice")
        else:
            print("Not noice")

    #def removePieceHighlight(self, key):