from CONSTANTS import *
import pygame
import copy
from pygame.locals import *

class Board():
    def __init__(self):
        grid = []
        for i in range(BOARDHEIGHT):
            grid.append([BLANK]*BOARDWIDTH)
        self.grid = grid
        self.gridBackup = None


    def update(self, piece):
        print('sb')
        self.gridBackup = copy.deepcopy(self.grid)
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if piece.structure[y][x] != BLANK:
                    self.grid[piece.y +y][piece.x + x] = piece.color

    def restore(self):
        self.grid =copy.deepcopy(self.gridBackup)

    def draw(self, canvas):
        # draw the border around the board
        pygame.draw.rect(canvas, BORDERCOLOR,
                         (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

        # fill the background of the board
        pygame.draw.rect(canvas, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
        # draw the individual boxes on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if self.grid[y][x] != BLANK:
                    pixelX = XMARGIN + x * BOXSIZE
                    pixelY = TOPMARGIN + y * BOXSIZE
                    pygame.draw.rect(canvas, COLORS[self.grid[y][x]],(pixelX + 1, pixelY + 1, BOXSIZE - 1, BOXSIZE - 1))
                    # draw shadow
                    pygame.draw.rect(canvas, COLORS[self.grid[y][x]],(pixelX + 1, pixelY + 1, BOXSIZE - 4, BOXSIZE - 4))

    def cancellingLine(self):
        pass
