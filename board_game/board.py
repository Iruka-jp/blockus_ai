from board_ui import Board_Ui
import numpy as np


class Board(object):
    def __init__(self, mode='classic'):

        if mode == 'duo':
            self.size = 14
        else:
            self.size = 20
        self.ui = Board_Ui(self.size)

        self.grid = np.zeros((self.size,self.size))



        # for i in range(1+self.size+2):
        #     for j in range(1+self.size):
        #         label = QLabel()
        #         if
        #             label.setFrameStyle(QFrame.Panel | QFrame.Plain)
        #             label.setLineWidth(2)
        #         self.grid.addWidget(label,i,j)
        # self.message = QLabel('Hello Blockus!')
        # self.message.alignment = Qt.AlignCenter

        # self.layout =
        # self.layout.addWidget(self.message)