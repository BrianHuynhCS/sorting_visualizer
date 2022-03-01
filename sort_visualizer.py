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
    SIDE_PAD = 100
    TOP_PAD = 150

    # width: width of display
    # height: height of display
    # list: list used for sorting 
    def __init__(self, width, height, list):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height)) # create display
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    # list: list
    # min_val: minimum value inside list
    # max_val: maximum value inside list
    # pixel_block_width: pixel width of each value inside list when represented as bar.
    # pixel_block_height: pixel height of each value inside list when represented as bar.
    def set_list(self, list):
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)
        self.pixel_block_width = round((self.width - self.SIDE_PAD) / len(list))
        self.pixel_block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

# Generate random list from range min_val to max_val of size n.
def generate_list(n, min_val, max_val):
    num = []
    for _ in range(n):
        value = random.randint(min_val, max_val)
        num.append(value)

    return num

# Run the display
def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 800, lst)

    pygame.display.update()

    while run:
        clock.tick(180)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()