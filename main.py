from Chess import Chess
from GUI import GUI

def Game():
    chess = Chess()
    print(chess.getBoard())
    gui = GUI(chess)
    
Game()