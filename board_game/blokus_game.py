from game_ui import Game_Ui
from board import Board
from player import  Player

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

        self.ui.layers.setCurrentIndex(1)

        #initialize players
        if mode=='duo':
            self.players = [Player() for i in range(2)]
        else:
            self.players = [Player() for i in range(4)]

        for i in range(5):
            for polyomino in self.players[0].hands[i]:
                self.ui.player_hand_scene.addPolygon(polyomino.graphic_items[0])

        self.ui.update()


