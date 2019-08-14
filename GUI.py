from tkinter import *
import os

class GUI:
    #app = gui("Chess", "600x600")
    __title = "Python chess!"
    __tileHighlight = "LawnGreen"
    __moveToHighlight = "SpringGreen"
    __lightTile = "#ffffff"
    __darkTile = "#000000"
    __imagePath = "\\Pieces\\Resources\\"
    __images = {"white": {
                    "King": "",
                    "Queen": "",
                    "Rook": "",
                    "Bishop": "",
                    "Knight": "",
                    "Pawn": ""
                },
                "black": {
                    "King": "",
                    "Queen": "",
                    "Rook": "",
                    "Bishop": "",
                    "Knight": "",
                    "Pawn": ""
                }}
    __tileButtons = {}

    def __init__(self, chess, ranks = 8, files = 8, GUIsize = 800):
        self.__GUIsize = GUIsize
        self.__ranks = ranks
        self.__files = files
        self.__chess = chess
        self.gui = Tk() # Initialize tkinter gui
        self.gui.geometry(str(self.__GUIsize) + "x" + str(self.__GUIsize)) # Set window size
        self.gui.resizable(False, False) # Set windown not resizable
        self.gui.title(self.__title) # Set window title
        self.__loadImages() # Load images from resources
        self.gui.iconphoto(False, self.__images["black"]["Pawn"]) # Set window icon
        #self.app.setSticky("news")
        #self.app.setExpand("both")
        #self.app.setFont(20)
        self.__setupGUI()

    def __setupGUI(self): 
        self.__margenHeight = int(self.__GUIsize * 0.1)
        self.__margenWidth = int(self.__GUIsize * 0.1)
        self.__buttonHeight = int((self.__GUIsize - self.__margenHeight) / self.__ranks) # x is out the ranks
        self.__buttonWidth = int((self.__GUIsize - self.__margenWidth) / self.__files) # y is up the files
        self.__selectedPiece = (-1,-1)
                   
        self.__drawGUI()
        #self.app.go()

    def __loadImages(self):
        for color in self.__images:
            for piece in self.__images[color]:
                #fullpath = os.getcwd() + self.__imagePath + color + "_" + piece.lower() + ".png"
                fullpath = os.getcwd() + self.__imagePath + color + "_" + "king" + ".png"
                self.__images[color][piece] = PhotoImage(file=fullpath)
                print(color, piece)
                print(self.__images[color][piece])

    # Draw GUI buttons
    def __drawGUI(self):
            #print("Updating all tiles")
            for rank in range(self.__ranks + 2):
                for file in range(self.__files + 2):
                    if (rank == 0 or rank == self.__ranks + 1):
                        Button(self.gui, text = 'F', bg = self.__lightTile, \
                            state = DISABLED, height = int(self.__margenHeight / 2), \
                            width = int(self.__margenWidth / 2), compound = CENTER) \
                            .place(x = int(file*self.__margenHeight), y = int((rank*self.__margenWidth)))
                        print("{},{}".format(rank, file))
                    elif (file == 0 or file == self.__files + 1):
                        Button(self.gui, text = 'F', bg = self.__lightTile, \
                            state = DISABLED, height = int(self.__margenHeight / 2), \
                            width = int(self.__margenWidth / 2), compound = CENTER) \
                            .place(x = int(file*self.__margenHeight), y = int((rank*self.__margenWidth)))
                        print("{},{}".format(rank, file))
                    else:
                        key = (rank - 1,file - 1) #self.getPieceName(key)
                        self.__tileButtons[key] = Button(self.gui, command = self.__getButtonCommand(key), \
                            bg = self.__getButtonColor(key), state = self.__getButtonState(key), \
                            height = self.__buttonHeight, width = self.__buttonWidth, \
                            image = self.__getButtonImage(key), compound = CENTER)
                        self.__tileButtons[key].place(x = int((file*self.__buttonHeight) + \
                            (self.__margenHeight / 2)),  y = int((rank*self.__buttonWidth) + \
                            (self.__margenWidth / 2)))
            #print(self.__tileButtons)

    # Update the GUI buttons
    def __updateGUI(self, moves = None, highlight = False):
        if (self.__selectedPiece != (-1,-1)):
            #print("Updating movable tiles: {}".format(moves))
            if (moves != None):
                for move in moves: 
                    self.__tileButtons[move].config(command = self.__getButtonCommand(move, highlight), \
                        bg = self.__getButtonColor(move, highlight), state = self.__getButtonState(move, highlight), \
                        image = self.__getButtonImage(move))
            #else:
                #print("Moves is None")

    def __onClick(self, key):
        #print(self.__selectedPiece)
        #print(key)
        #print("Click on key {}".format(key))
        if (self.__selectedPiece != (-1,-1)):
            #print("Attemting to move {} to position {}".format(self.__selectedPiece, key))
            # Ask Chess.py to move piece. Chess.py will return true if piece was moved, false if not.
            moves = self.__chess.getAvaliableMoves(self.__selectedPiece) # List of tiles to cleanup after move
            if (self.__chess.movePieceByKey(self.__selectedPiece, key)):
                moves.append(self.__selectedPiece) # Piece moved succesfully, append to cleanup list
                #print("Moved piece")
            #else:
                #print("Invalid move")
            self.__updateGUI(moves) # Clean GUI
            self.__selectedPiece = (-1,-1) # Reset selected key
        elif (self.__chess.getPiece(key) != None):
            moves = self.__chess.getAvaliableMoves(key)
            if (moves != None):
                #print("{} can move to {}".format(key, moves))
                self.__selectedPiece = key
                self.__updateGUI(moves, True) # Highlight movable tiles
            else:
                #print("No valid moves avaliable")
                self.__selectedPiece = (-1,-1)
        else:
            self.__selectedPiece = (-1,-1)
            #print("Not a piece or valid move")

    def __getButtonColor(self, key, highlight = False):
        if (highlight):
            return self.__tileHighlight
        else:
            return self.__getChessboardPattern(key)

    def __getButtonImage(self, key):
        if (self.__chess.getPiece(key) != None):
            return self.__images[self.__chess.getPiece(key).getColor()][self.__chess.getPiece(key).getType()]
        else:
            return ''

    def __getButtonCommand(self, key, override = False):
        if (self.__chess.getPiece(key) != None or override):
            return (lambda: self.__onClick(key))
        else:
            return None

    def __getButtonState(self, key, override = False):
        if (self.__chess.getPiece(key) != None or override):
            return NORMAL
        else:
            return DISABLED

    def __getChessboardPattern(self, key):
        if key[0]%2 == 0 and key[1]%2 == 0:
            return self.__lightTile
        elif key[0]%2 == 1 and key[1]%2 == 0:
            return self.__darkTile
        elif key[0]%2 == 0 and key[1]%2 == 1:
            return self.__darkTile
        else:
            return self.__lightTile