import numpy as np

class Polyomino():
    def __init__(self, shape:np.array):
        self.shape = shape
        self.representations = self.variations()

    def variations(self):
        variations = []
        for i in range(0,4):
            var = np.rot90(self.shape,i)
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


polyominoes = [
    [
        Polyomino(np.array([[1]]))
    ],[
        Polyomino(np.array([[1, 1]]))
    ],[
        Polyomino(np.array([[1, 1, 1]])),
        Polyomino(np.array([[1, 1],
                           [1, 0]]))
    ],[
        Polyomino(np.array([[1, 1, 1, 1]])),
        Polyomino(np.array([[1, 1, 1],
                           [1, 0, 0]])),
        Polyomino(np.array([[1, 1, 1],
                           [0, 1, 0]])),
        Polyomino(np.array([[1, 1, 0],
                           [0, 1, 1]])),
        Polyomino(np.array([[1, 1],
                           [1, 1]])),
    ],[
        Polyomino(np.array([[1, 1, 1, 1, 1]])),
        Polyomino(np.array([[1, 1, 1, 1],
                           [1, 0, 0, 0]])),
        Polyomino(np.array([[1, 1, 1, 1],
                           [0, 1, 0, 0]])),
        Polyomino(np.array([[1, 1, 0, 0],
                           [0, 1, 1, 1]])),
        Polyomino(np.array([[1, 1, 1],
                           [0, 1, 1]])),
        Polyomino(np.array([[1, 1, 1],
                           [1, 0, 1]])),
        Polyomino(np.array([[1, 1, 1],
                           [1, 0, 0],
                           [1, 0, 0]])),
        Polyomino(np.array([[1, 1, 1],
                           [0, 1, 0],
                           [0, 1, 0]])),
        Polyomino(np.array([[0, 1, 1],
                           [0, 1, 0],
                           [1, 1, 0]])),
        Polyomino(np.array([[0, 1, 1],
                           [1, 1, 0],
                           [1, 0, 0]])),
        Polyomino(np.array([[0, 1, 0],
                           [1, 1, 1],
                           [1, 0, 0]])),
        Polyomino(np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])),
    ],
]

if __name__ == "__main__":
    poly = Polyomino(np.array([[1, 1]]))
    print(poly.representations)
    poly = Polyomino(np.array([[1, 1, 1],
              [1, 0, 0],
              [1, 0, 0]]))
    for r in poly.representations: print(r)

