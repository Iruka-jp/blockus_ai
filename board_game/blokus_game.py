from game_ui import Game_Ui
from board import Board
from polyomino import polyominoes

class Blokus(object):
    def __init__(self):
        self.ui = Game_Ui()

        # connect signals
        self.ui.start_game.clicked.connect(lambda: self.initialize_game('duo')) #to be modified
        self.ui.quit_game.clicked.connect(self.ui.close)

    def initialize_game(self, mode):

        #initialize board game
        self.board = Board(mode=mode)
        self.ui.grid.addWidget(self.board.ui, 0, 0)
        self.ui.update()
        self.ui.layers.setCurrentIndex(1)

        #initialize players
        if mode=='duo':
            self.players_moves = [[],[]]
            self.players_polyominoes = [polyominoes, polyominoes]
        else:
            self.players_moves = [[], [],[],[]]
            self.players_polyominoes = [polyominoes, polyominoes, polyominoes, polyominoes]


