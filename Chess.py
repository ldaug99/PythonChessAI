from Pieces.Pawn import Pawn as Pawn
from Pieces.Knight import Knight as Knight
from Pieces.Bishop import Bishop as Bishop
from Pieces.Rook import Rook as Rook
from Pieces.Queen import Queen as Queen
from Pieces.King import King as King

class Chess:
    __ranks = 8
    __files = 8
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
            self.__chessboard[1,i] = Pawn(self.__black)
            self.__chessboard[6,i] = Pawn(self.__white)
            self.__chessboard[0,i] = lineup[i](self.__black)
            self.__chessboard[7,i] = lineup[i](self.__white)    

    def __noneChessboard(self):
        for i in range(0,self.__ranks):
            for k in range (0,self.__files):
                self.__chessboard[i,k] = None
    
    def getBoard(self):
        return self.__chessboard

    def getPiece(self, key):
        return self.__chessboard[key]
    
    def getKeys(self):
        return list(self.__chessboard.keys())

    def getKeyFromPiece(self, piece):
        if piece != None:
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
    
    def getAvaliableMoves(self, key, desiredMove = None):
        moves = None
        if (desiredMove != None):
            moves = desiredMove
        else:
            moves = self.__chessboard[key].getMoves(key)
        for move in moves:
            piece = self.getPiece(move)
            if (piece != None):
                if (piece.getColor() == self.getPiece(key).getColor()):
                    moves.remove(move)
            elif (move[0] > self.__ranks or move[0] < 0 or move[1] > self.__files or move[1] < 0):
                moves.remove(move)
        return moves

    def movePieceByKey(self, fromKey, toKey):
        if (fromKey == toKey):
            return False
        else:
            # Check if there is a piece at position
            # Check if piece can move in the selected pattern
            # Check if piece was taken
            self.__chessboard[toKey] = self.__chessboard[fromKey]
            self.__chessboard[fromKey] = None
            return True
            # Check if checkmate

    def getKeyByMatrix(self, _rank, _file):
        # rank is row, file is column as with matrices
        return [_rank, _file]

    def getMovesByKey(self, key):
        piece = self.__chessboard[key]
        if piece != None:
            return piece.getMoves(self.getKeyFromPiece(piece))
        return None
    
    def isMoveValid(self, fromKey, toKey):
        if fromKey != None:
            pass