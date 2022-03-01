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

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    # width: width of display
    # height: height of display
    # list: list used for sorting 
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height)) # create display
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    # list: list
    # min_val: minimum value inside list
    # max_val: maximum value inside list
    # pixel_block_width: pixel width of each value inside list when represented as bar.
    # pixel_block_height: pixel height of each value inside list when represented as bar.
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.pixel_block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.pixel_block_height = int((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

# Method for drawing window
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    # regular controls
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 5))

    # sorting controls
    controls = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 35))
    draw_list(draw_info)
    pygame.display.update()

# Method for drawing list
def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.pixel_block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.pixel_block_height

        color = draw_info.GREY
        
        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.pixel_block_width, draw_info.height))
    
    if clear_bg:
        pygame.display.update()

# Generate random list from range min_val to max_val of size n.
def generate_list(n, min_val, max_val):
    num = []
    for _ in range(n):
        value = random.randint(min_val, max_val)
        num.append(value)

    return num

# bubble sort algorithm
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        lst = draw_info.lst
        for j in range(len(lst)- 1- i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
                # generator to draw list
                yield True

    return lst


# Run the display
def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 600, lst)

    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algo_name = "bubble sort"
    sorting_algorithm_generator = None

    pygame.display.update()

    while run:
        clock.tick(180)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
    pygame.quit()

if __name__ == "__main__":
    main()