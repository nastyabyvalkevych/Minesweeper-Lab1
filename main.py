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

    def create_custom_theme(self):
        theme = pygame_menu.themes.THEME_DEFAULT.copy()
        theme.title_font = pygame_menu.font.FONT_NEVIS
        theme.widget_font = pygame_menu.font.FONT_COMIC_NEUE
        theme.widget_font_size = 25
        theme.title_font_color = (80, 80, 90)
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        return theme


    def display_main_menu(self):

        main_menu_theme = self.create_custom_theme()

        self.main_menu = pygame_menu.Menu('Minesweeper', self.width, self.height, theme=main_menu_theme)
        self.image_widget = self.main_menu.add.image(
            image_path="background2.png",
            padding=(0, 0, 30, 0)
            # top, right, bottom, left
            # top, right, bottom, left
        )
        self.main_menu.add.text_input('Name: ', default='username', maxchar=20)
        # Add a sub-menu for 'Play'
        play_menu = self.add_play_menu()
        self.main_menu.add.button('Play', play_menu)
        # Add a sub-menu for 'About'
        about_menu = self.add_about_menu()
        self.main_menu.add.button('About', about_menu)
        self.main_menu.mainloop(self.window, fps_limit=fps)

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
