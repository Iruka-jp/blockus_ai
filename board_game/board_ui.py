from PySide6.QtWidgets import QWidget, QLabel, QLayoutItem, QGridLayout, QFrame
from PySide6.QtGui import QPainter, QPixmap, QColor, QPen
from PySide6.QtCore import Qt

CELL_WIDTH=40
CELL_HEIGHT=40

class Board_Ui(QWidget):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.resize(self.size*CELL_WIDTH+1, self.size*CELL_HEIGHT+1)
        self.update()

    def paintEvent(self,event):

        painter = QPainter(self)
        pen = QPen(Qt.black)
        painter.setPen(pen)
        for i in range(self.size+1):
            painter.drawLine(CELL_WIDTH*i,0,CELL_WIDTH*i, self.size*CELL_HEIGHT)
            painter.drawLine(0, CELL_HEIGHT*i, self.size*CELL_WIDTH, CELL_HEIGHT*i)
        self.update()