import numpy as np
from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPoint
from utils import nearest_neighbor

class Polyomino():
    def __init__(self, body:np.array):
        self.body = body
        self.representations = self.variations()
        self.graphic_items = self.create_graphics()

    def padding(self):
        rep = np.zeros([self.body.shape[0] + 2, self.body.shape[1] + 2])
        for i in range(self.body.shape[0]):
            for j in range(self.body.shape[1]):
                rep[i + 1, j + 1] = self.body[i, j]
        return rep

    def variations(self):
        variations = [self.padding()]
        for i in range(0,4):
            var = np.rot90(variations[0],i)
            var1 = np.flip(var, axis=0)
            new = True
            for array in variations:
                if np.array_equal(array, var):
                    new = False
                    break
            if new: variations.append(var)
            for array in variations:
                if np.array_equal(array, var1):
                    new = False
                    break
            if new: variations.append(var1)
        return variations



    def create_graphics(self):
        graphic_items = []
        self.contour = []
        for rep in self.representations:
            points = []
            for i in range(rep.shape[0]):
                for j in range(rep.shape[1]):
                    if rep[i, j] == 1:
                        points.append((i, j))
                        points.append((i, j + 1))
                        points.append((i + 1, j))
                        points.append((i + 1, j + 1))

            points = sorted(points)

            to_remove = set()
            for i in range(len(points) - 1):
                if points[i] == points[i + 1]:
                    try:
                        if points[i] == points[i + 3]:
                            to_remove.update([i, i + 1, i + 2, i + 3])
                        else:
                            to_remove.add(i + 1)
                    except IndexError:
                        to_remove.add(i + 1)

            to_remove = sorted(to_remove)
            for t, i in enumerate(to_remove):
                points.pop(i - t)

            contour = []
            contour.append(points.pop(0))
            while len(points) > 0:
                idx = nearest_neighbor(contour, points, rep)
                contour.append(points.pop(idx))

            to_remove=[]
            for i in range(len(contour)-2):
                if contour[i][0] == contour[i+1][0] == contour[i+2][0]:
                    to_remove.append(i+1)
                elif contour[i][1] == contour[i+1][1] == contour[i+2][1]:
                    to_remove.append(i+1)

            for t, i in enumerate(to_remove):
                contour.pop(i-t)


            for i in range(len(contour)):
                contour[i] = QPoint(20*contour[i][0], 20*contour[i][1])

            graphic_items.append(QPolygonF(contour))
        return graphic_items







if __name__ == "__main__":
    poly = Polyomino(np.array([[1, 1, 1],
								[1, 0, 1]]))
    print(poly.representations[0])
    print(poly.graphic_items[0])

