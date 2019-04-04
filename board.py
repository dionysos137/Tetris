from CONSTANTS import *
import pygame
import copy
import numpy as np
from pygame.locals import *

class Board():
    def __init__(self,h, w, pieceSize):
        # construct the abstract layer which encodes which point is occupied
        # 1 | 0 | 1
        # 1 | 0 | 1
        # 1 | 1 | 1
        full = np.ones([h+2*pieceSize, w+2*pieceSize], dtype='int')
        full[:h+pieceSize, pieceSize:w+pieceSize] = 0
        self.height = h
        self.width = w
        self.abstractLayer = full
        self.pieceSize = pieceSize

        # the physicalLayer will encode the color info which will be drawn on the screen
        self.physicalLayer = np.zeros([h+2*pieceSize, w+2*pieceSize], dtype='int')
        self.abstractLayerBackup = None
        self.physicalLayerBackup = None


    def save(self):
        self.abstractLayerBackup = copy.deepcopy(self.abstractLayer)
        self.physicalLayerBackup = copy.deepcopy(self.physicalLayer)
    def update(self, piece):
        pieceSize = piece.structure.shape[0]
        self.abstractLayer[pieceSize+piece.y:piece.y+2*pieceSize, pieceSize+piece.x:piece.x+2*pieceSize] += piece.structure
        self.physicalLayer[pieceSize+piece.y:piece.y+2*pieceSize, pieceSize+piece.x:piece.x+2*pieceSize] += piece.colored

    def get_board(self):
        """get the w*h part of the physical layer
                """

        return self.physicalLayer[self.pieceSize:self.pieceSize+self.height, self.pieceSize:self.pieceSize+self.width]

    def restore(self):
        self.abstractLayer = copy.deepcopy(self.abstractLayerBackup)
        self.physicalLayer = copy.deepcopy(self.physicalLayerBackup)

    def draw(self, canvas):
        # draw the border around the board
        pygame.draw.rect(canvas, BORDERCOLOR,
                         (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

        # fill the background of the board
        pygame.draw.rect(canvas, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
        # draw the individual boxes on the board
        boardToDraw = self.get_board()
        for x in range(self.width):
            for y in range(self.height):
                if boardToDraw[y, x] != 0:
                    pixelX = XMARGIN + x * BOXSIZE
                    pixelY = TOPMARGIN + y * BOXSIZE
                    pygame.draw.rect(canvas, COLORS[boardToDraw[y, x]-1],(pixelX + 1, pixelY + 1, BOXSIZE - 1, BOXSIZE - 1))
                    # draw shadow
                    pygame.draw.rect(canvas, COLORS[boardToDraw[y, x]-1],(pixelX + 1, pixelY + 1, BOXSIZE - 4, BOXSIZE - 4))

    def cancellingLine(self):
        pass
