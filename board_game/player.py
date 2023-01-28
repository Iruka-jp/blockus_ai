from polyomino import Polyomino
import numpy as np


class Player(object):

    def __init__(self):
        self.hands = [
            [
                Polyomino(np.array([[1]]))
            ], [
                Polyomino(np.array([[1, 1]]))
            ], [
                Polyomino(np.array([[1, 1, 1]])),
                Polyomino(np.array([[1, 1],
                                    [1, 0]]))
            ], [
                Polyomino(np.array([[1, 1, 1, 1]])),
                Polyomino(np.array([[1, 1, 1],
                                    [1, 0, 0]])),
                Polyomino(np.array([[1, 1, 1],
                                    [0, 1, 0]])),
                Polyomino(np.array([[1, 1, 0],
                                    [0, 1, 1]])),
                Polyomino(np.array([[1, 1],
                                    [1, 1]])),
            ], [
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

        self.moves = []
