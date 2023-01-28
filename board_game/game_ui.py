from PySide6 import QtWidgets
from PySide6.QtCore import Qt

class Game_Ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layers = QtWidgets.QStackedWidget(self)
        WIDTH = 1000
        HEIGHT = 1000
        self.resize(WIDTH,HEIGHT)

        # Start view
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName('Start page')
        self.start_page_vl = QtWidgets.QVBoxLayout(self.start_page)
        self.start_game = QtWidgets.QPushButton(self.start_page)
        self.start_game.setText('Start game')
        self.start_game.setFixedSize(200,50)
        self.load_game = QtWidgets.QPushButton(self.start_page)
        self.load_game.setText('Load game')
        self.load_game.setFixedSize(200, 50)
        self.quit_game = QtWidgets.QPushButton(self.start_page)
        self.quit_game.setText('Quit')
        self.quit_game.setFixedSize(200, 50)

        self.start_page_vl.addSpacing(100)
        title = QtWidgets.QLabel('Let\'s play Blokus!')
        title.setAlignment(Qt.AlignCenter)
        self.start_page_vl.addWidget(title)
        self.start_page_vl.addSpacing(100)

        hl = QtWidgets.QHBoxLayout()
        hl.addSpacing(400)
        hl.addWidget(self.start_game)
        hl.addSpacing(400)
        self.start_page_vl.addLayout(hl)

        self.start_page_vl.addSpacing(100)

        hl = QtWidgets.QHBoxLayout()
        hl.addSpacing(400)
        hl.addWidget(self.load_game)
        hl.addSpacing(400)
        self.start_page_vl.addLayout(hl)

        #self.start_page_vl.addWidget(self.load_game)
        self.start_page_vl.addSpacing(100)
        hl = QtWidgets.QHBoxLayout()
        hl.addSpacing(400)
        hl.addWidget(self.quit_game)
        hl.addSpacing(400)
        self.start_page_vl.addLayout(hl)


        self.layers.addWidget(self.start_page)

        # Game view
        self.grid = QtWidgets.QGridLayout()
        self.grid.setColumnMinimumWidth(0,600)
        self.grid.setRowMinimumHeight(0,600)

        self.board_scene = QtWidgets.QGraphicsScene()
        board_view = QtWidgets.QGraphicsView(self.board_scene, self)
        self.grid.addWidget(board_view, 1, 0)

        label = QtWidgets.QLabel('Information')
        label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(label, 0, 1)


        self.player_hand_scene = QtWidgets.QGraphicsScene()
        player_hand_view = QtWidgets.QGraphicsView(self.player_hand_scene, self)
        # player_hand_view.setFixedSize(400,200)
        self.grid.addWidget(player_hand_view, 1, 0)
        self.grid.setRowMinimumHeight(1, 300)

        label = QtWidgets.QLabel('others')
        label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(label, 1, 1)

        self.play_page = QtWidgets.QWidget()
        self.play_page.setLayout(self.grid)
        self.layers.addWidget(self.play_page)