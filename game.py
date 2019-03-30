from piece import Piece
from board import Board
from utils import displayTextScreen
from CONSTANTS import *
import time
import pygame
import sys
from pygame.locals import *

FallFreq = 0.2

def run_game(screen):

    # initialize the board
    board = Board()
    # initialize two pieces
    fallingPiece = Piece()
    nextPiece = Piece()
    # initialize times
    [lastFallTime, lastMoveDown, lastMoveSidewaysTime] = [time.time()] * 3

    while True: #game loop
        # if the last piece has fallen, the nextPiece becomes the new falling piece
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = Piece()
            lastFallTime = time.time() #?
            # if the fallingPiece cannot fall anymore, game is over
            if not fallingPiece.isValidPosition(board):
                return

        # keyboard event
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.quit()
            if event.type == KEYDOWN:
                # pause
                if event.key == K_p:
                    screen.fill(BGCOLOR)
                    #pygame.mixer.music.stop()
                    displayTextScreen('Paused', screen)  # pause until a key press
                    #pygame.mixer.music.play(-1, 0.0)
                    [lastFallTime, lastMoveDown, lastMoveSidewaysTime] = [time.time()]*3

                # move
                elif event.key == K_LEFT and fallingPiece.isValidPosition(board,'L'):
                    fallingPiece.move_left()
                    print("left")

                elif event.key == K_RIGHT and fallingPiece.isValidPosition(board, 'R'):
                    fallingPiece.move_right()
                    print("right")

                elif event.key == K_DOWN and fallingPiece.isValidPosition(board, 'D'):
                    fallingPiece.move_down()
                    print("down")
                    lastFallTime = time.time()

        if time.time() - lastFallTime > FallFreq and fallingPiece.isValidPosition(board, 'D'):
            fallingPiece.move_down()
            print('down')
            lastFallTime = time.time()

        # if it reach the bottom
        if not fallingPiece.isValidPosition(board, 'D'):
            board.update(fallingPiece)
            score = score + board.cancellingLine()
            #level, FallFreq = difficulty(score)


        screen.fill(BGCOLOR)
        board.update(fallingPiece)
        board.draw(screen)
        board.restore()
        pygame.display.update()



