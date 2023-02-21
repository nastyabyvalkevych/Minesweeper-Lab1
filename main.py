import pygame
from pygame.locals import *
import pygame_menu
from pygame_menu import themes
import random
import math


pygame.init()

# frames per second
fps = 120

# width and height of each cell
cell_size = 50

# height of the panel containing the timer and flag count
top_panel_height = 50

# values for mouse click event
left_mouse_click = 1
right_mouse_click = 3

# font for displaying clues, time, and flag count
font = pygame.font.Font(pygame.font.get_default_font(), 18)


#define colors for displaying clues
clue_colors = ['', 'blue', 'chartreuse4', 'purple', 'red', 'green', 'turquoise', 'black']

ABOUT = ['pygame-minesweeper',
         'Authors: Nastya & Danya',
         'Email: .....']

class Game:
    def __init__(self):
        self.height = None
        self.width = None
        self.set_difficulty('beginner')
        self.setup_window()

        # declare the menus and display the new game menu
        self.main_menu = None
        self.about_menu = None
        self.play_menu = None
        self.gameover_menu = None
        self.display_main_menu()

    def set_difficulty(self, difficulty):

        if difficulty == 'beginner':
            self.size = {'rows': 8, 'cols': 8}
            self.num_mines = 10
        elif difficulty == 'intermediate':
            self.size = {'rows': 16, 'cols': 16}
            self.num_mines = 40
        elif difficulty == 'expert':
            self.size = {'rows': 16, 'cols': 30}
            self.num_mines = 99

    def setup_window(self):
        self.width = cell_size * self.size['cols']
        self.height = cell_size * self.size['rows'] + top_panel_height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Minesweeper')
        # useless code
        background_image = pygame.image.load("background2.png")
        self.window.blit(background_image, (0, 0))

class Cell(pygame.Rect):
    pass


def main():
    # create the game
    game = Game()

    # game loop
    clock = pygame.time.Clock() #створити об’єкт, який допоможе відстежувати час
    running = True
    while running:

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
