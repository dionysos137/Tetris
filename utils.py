import sys
import pygame
from pygame.locals import *
from CONSTANTS import *



def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        pygame.quit()
        sys.exit() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
            # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    # for event in pygame.event.get(KEYDOWN):
    #     return event.key
    #
    # return None
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            return event.key
    return None
    #
    # for event in pygame.event.get([KEYDOWN, KEYUP]):
    #     if event.type == KEYDOWN:
    #         continue
    #     return event.key
    # return None


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def displayTextScreen(text, screen):
    # display text in the center of screen
    # until another key is pressed

    # draw the shadow
    shadowSurf, shadowRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    shadowRect.center = (int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2))
    screen.blit(shadowSurf, shadowRect)

    # draw the text
    textSurf, textRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    textRect.center = (int(WINDOWWIDTH / 2-3), int(WINDOWHEIGHT / 2-3))
    screen.blit(textSurf, textRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    screen.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()

