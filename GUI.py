from tkinter import *
class GUI:
    gui = None
    #app = gui("Chess", "600x600")
    __GUISize = 800
    __tileHighlight = "LawnGreen"
    __moveToHighlight = "SpringGreen"
    __lightTile = "#ffffff"
    __darkTile = "#000000"
    __chessboard = {}
    __selectedPiece = "(-1,-1)"
    __movingPiece = False

    def __init__(self, chessboard, ranks = 8, files = 8):
        self.gui = Tk()
        GUISize = str(self.__GUISize) + "x" + str(self.__GUISize)
        self.gui.geometry(GUISize)
        #self.app.setSticky("news")
        #self.app.setExpand("both")
        #self.app.setFont(20)
        self.__ranks = ranks
        self.__files = files
        self.__chessboard = chessboard
        self.setupGUI()

    def setupGUI(self):              
        self.drawGUI()
        #self.app.go()

    def buttonCallback(self, key):
        return (lambda: self.onClick(key))

    def onClick(self, key):
        #value = var.get()
        #key = self.labelToKey(label)
        print("Click on key (" + str(key[0]) + "," + str(key[1]) + ")")
        
        """
        if label == self.__movingPiece:
            self.drawGUI()
            self.__selectedPiece = "(-1,-1)"
        elif self.__selectedPiece != "(-1,-1)":
            validMove = False
            moves = self.getPieceMoves(key)
            for i in range(len(moves)):
                if label == moves[i]:
                    validMove = True
            if validMove:
                print("Moving piece")
                # Move piece
            else:
                self.drawGUI()
                self.__selectedPiece = "(-1,-1)"
        else:
            if self.__chessboard[key] != None:
                self.drawGUI(label)
                self.__selectedPiece = label
        """

    def drawGUI(self, selectedLabel = None):
        if selectedLabel != None:
            key = self.labelToKey(selectedLabel)
            moves = self.getPieceMoves(key)
        buttonHeight = int(self.__GUISize / self.__ranks) # x is out the ranks
        buttonWidth = int(self.__GUISize / self.__files) # y is out the files
        for i in range(self.__ranks):
            for k in range(self.__files):
                key = (i,k) #self.getPieceName(key)
                if self.isKeyBoundToPiece(key):
                    Button(self.gui, command = self.buttonCallback(key), \
                        bg = self.__getChessboardPattern(key), \
                        height = buttonHeight, width = buttonWidth, \
                        image = self.getPieceImage(key), compound = CENTER) \
                        .place(x = int(i*buttonHeight), y = int(k*buttonWidth))   
                else:
                    Button(self.gui, command = self.buttonCallback(key), \
                        bg = self.__getChessboardPattern(key), \
                        height = buttonHeight, width = buttonWidth, \
                        compound = CENTER) \
                        .place(x = int(i*buttonHeight), y = int(k*buttonWidth))
                    #button.grid(row=i,column=k)
                #str() 

                """
                key = (i,k)
                label = str(i) + str(k)
                highlightLabel = False
                if selectedLabel != None:
                    for h in range(len(moves)):
                        if label == self.keyToLabel(moves[h]):
                            highlightLabel = True
                self.app.addLabel(label, self.getPieceCharacter(key), i, k)
                if label == selectedLabel:
                    self.setTileColor(label, self.__tileHighlight)
                elif highlightLabel:
                    self.setTileColor(label, self.__moveToHighlight)
                else:
                    self.setTileColor(label, self.__getChessboardPattern(key))
                self.setPieceColor(label, self.getPieceColor(key))
                if self.__chessboard[self.labelToKey(label)] != None or highlightLabel:
                    self.makeClickable(label)
                """

    def isKeyBoundToPiece(self, key):
        if self.__chessboard[key] != None:
            return True
        else:
            return False
    
    def getPieceImage(self, key):
        return PhotoImage(file=(self.__chessboard[key] \
            .getImage()[self.__chessboard[key].getColor()]))

    """
    def getPieceCharacter(self, key):
        if self.isKeyBoundToPiece(key):
            return str(self.__chessboard[key].getCharacter() \
                [self.__chessboard[key].getColor()])
        else:
            return ""

    def getPieceName(self, key):
        if self.isKeyBoundToPiece(key):
            return str(self.__chessboard[key].getType())
        else:
            return ""
    """

    def __getChessboardPattern(self, key):
        if key[0]%2 == 0 and key[1]%2 == 0:
            return self.__lightTile
        elif key[0]%2 == 1 and key[1]%2 == 0:
            return self.__darkTile
        elif key[0]%2 == 0 and key[1]%2 == 1:
            return self.__darkTile
        else:
            return self.__lightTile

    """
    def drawGUI(self, selectedLabel = None):
        self.app.emptyCurrentContainer()
        if selectedLabel != None:
            key = self.labelToKey(selectedLabel)
            moves = self.getPieceMoves(key)
        for i in range(self.__ranks):
            for k in range(self.__files):
                key = (i,k)
                label = str(i) + str(k)
                highlightLabel = False
                if selectedLabel != None:
                    for h in range(len(moves)):
                        if label == self.keyToLabel(moves[h]):
                            highlightLabel = True
                self.app.addLabel(label, self.getPieceCharacter(key), i, k)
                if label == selectedLabel:
                    self.setTileColor(label, self.__tileHighlight)
                elif highlightLabel:
                    self.setTileColor(label, self.__moveToHighlight)
                else:
                    self.setTileColor(label, self.__getChessboardPattern(key))
                self.setPieceColor(label, self.getPieceColor(key))
                if self.__chessboard[self.labelToKey(label)] != None or highlightLabel:
                    self.makeClickable(label)
    """

    #def makeClickable(self, label):
        #self.app.setLabelSubmitFunction(label, self.onClick)

    def resetGUI(self):
        for i in range(self.__ranks):
            for k in range(self.__files):
                label = str(i) + str(k)

    """
    def getPieceMoves(self, key):
        return self.__chessboard[key].getMoves(key)

    def setColorProfile(self, light, dark, highlight):
        self.__lightTile = light
        self.__darkTile = dark
        self.__tileHighlight = highlight




    
    def getPieceColor(self, key):
        if self.__getChessboardPattern(key) == self.__darkTile:
            return self.__lightTile
        else:
            return self.__darkTile

    def labelToKey(self, label):
        return (int(label[0]),int(label[1]))

    def keyToLabel(self, key):
        return str(key[0]) + str(key[1])

    def setTileColor(self, label, color):
        self.app.setLabelBg(label, color)

    def setPieceColor(self, label, color):
        self.app.setLabelFg(label, color)

    #def removePieceHighlight(self, key):
    """
