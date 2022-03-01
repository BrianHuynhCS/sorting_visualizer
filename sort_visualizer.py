import pygame
import random
pygame.init()

# color variables
class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

# width: width of display
# height: height of display
# list: list used for sorting 
def __init__(self, width, height, list):
    self.width = width
    self.height = height

    self.window = pygame.display.set_mode((width, height)) # create display
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    self.set_list(list)