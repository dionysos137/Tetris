import random
import numpy as np
import copy
from CONSTANTS import *


S_SHAPE_TEMPLATE = [np.array([
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,1,1,0],
                     [0,1,1,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,0,1,1,0],
                     [0,0,0,1,0],
                     [0,0,0,0,0]])
                    ]

Z_SHAPE_TEMPLATE = [np.array([
                     [0,0,0,0,0],
                     [0,1,1,0,0],
                     [0,0,1,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,1,1,0,0],
                     [0,1,0,0,0],
                     [0,0,0,0,0]])
                    ]

I_SHAPE_TEMPLATE = [np.array([
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [1,1,1,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]])
                    ]


O_SHAPE_TEMPLATE = [np.array([
                     [0,0,0,0,0],
                     [0,1,1,0,0],
                     [0,1,1,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]])
                    ]


J_SHAPE_TEMPLATE = [np.array([
                     [0,0,0,0,0],
                     [0,1,0,0,0],
                     [0,1,1,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,1,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,1,1,1,0],
                     [0,0,0,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,1,1,0,0],
                     [0,0,0,0,0]])
                    ]


L_SHAPE_TEMPLATE = [np.array([
                     [0,0,0,0,0],
                     [0,0,0,1,0],
                     [0,1,1,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,1,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,1,1,1,0],
                     [0,1,0,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,1,1,0,0],
                     [0,0,1,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]])
                    ]

T_SHAPE_TEMPLATE = [np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,1,1,1,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,0,1,1,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,1,1,1,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]]),
                    np.array([
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,1,1,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]])
                    ]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

class Piece():

    def __init__(self):

        self.x = int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2)
        self.y = -2
        self.shape = random.choice(list(PIECES.keys()))
        self.state = random.randint(0, len(PIECES[self.shape])-1)
        self.color = random.randint(1, len(COLORS))
        self.structure = copy.deepcopy(PIECES[self.shape][self.state])
        colored = copy.deepcopy(PIECES[self.shape][self.state])
        colored[colored == 1] = self.color
        self.colored = colored



    def isValidPosition(self, board, dir):
        """

        :param board:
        :param dir: "L", "R", "D"
        :return:
        """
        if dir == "L":
            #coordinate after (hypethetically) move to the left
            newX = self.x - 1
            newY = self.y


        elif dir == "R":
            # coordinate after (hypethetically) move to the right
            newX = self.x + 1
            newY = self.y


        elif dir == "D":
            # coordinate after (hypethetically) move to the left
            newX = self.x
            newY = self.y + 1

        newLayer = copy.deepcopy(board.abstractLayer)
        newLayer[board.pieceSize + newY:2 * board.pieceSize + newY,
        board.pieceSize + newX:2 * board.pieceSize + newX] += self.structure
        if np.any(newLayer > 1):
            return False
        else:
            return True



    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_down(self):
        self.y += 1



