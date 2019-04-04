import random, time, pygame, sys
from pygame.locals import *
from utils import displayTextScreen
from CONSTANTS import *
from game import run_game



def main():
    pygame.init()
    # create screen
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Tetromino")
    displayTextScreen("Tretromino", screen)
    run_game(screen)
    # running = True
    # while running:
    #     # load background music
    #     if random.randint(0, 1) == 0:
    #         pygame.mixer.music.load('tetrisb.mid')
    #     else:
    #         pygame.mixer.music.load('tetrisc.mid')
    #
    #     pygame.mixer.music.play(-1, 0.0)
    #     run_game()
    #     pygame.mixer.music.stop()
    displayTextScreen('Game Over')


if __name__ == "__main__":
    main()

