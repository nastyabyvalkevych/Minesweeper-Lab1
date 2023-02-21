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

    def get_clicked_cell(self, click_location):

        # iterate through every cell
        for (row, col) in self.cells:
            cell = self.cells[(row, col)]

            # check if that cell was clicked
            if cell.collidepoint(click_location):
                return cell

        # no cell was clicked
        return None

    def left_click(self, click_location):

        # do nothing if the game is over
        if self.gameover:
            return

        clicked_cell = self.get_clicked_cell(click_location)

        if clicked_cell is not None:

            # check if this is the first click of the game
            if self.revealed_count == 0:
                self.place_mines(clicked_cell)
                self.update_clues()

            # reveal the cell and increment the revealed_count
            self.revealed_count += clicked_cell.reveal(self.cells)

            # game is over if the clicked cell has a mine
            if clicked_cell.has_mine:
                self.gameover = True

            # check if the game is cleared
            if self.revealed_count == self.size['rows'] * self.size['cols'] - self.num_mines:
                self.gameover = True
                self.display_gameover_menu('Game Cleared')

    def place_mines(self, clicked_cell):

        # create mines at random locations
        mine_count = 0
        while mine_count < self.num_mines:
            row = random.randint(0, self.size['rows'] - 1)
            col = random.randint(0, self.size['cols'] - 1)
            mine_cell = self.cells[(row, col)]

            # calculate distance between mine and the clicked cell
            distance = math.sqrt((row - clicked_cell.row) ** 2 + (col - clicked_cell.col) ** 2)

            # place mine only if it's more than two cells away from the clicked cell
            # and the location doesn't already have a mine
            if distance > 2 and mine_cell.has_mine == False:
                mine_cell.has_mine = True
                mine_count += 1

    def update_clues(self):

        # iterate through every cell
        for (row, col) in self.cells:
            cell = self.cells[(row, col)]

            # check the surrounding cells
            for adjacent_row in range(row - 1, row + 2):
                for adjacent_col in range(col - 1, col + 2):

                    # no need to check same cell
                    if cell.row == adjacent_row and cell.col == adjacent_col:
                        continue

                    # check if adjacent location has a mine
                    if (adjacent_row, adjacent_col) in self.cells:
                        adjacent_cell = self.cells[(adjacent_row, adjacent_col)]
                        if adjacent_cell.has_mine:
                            cell.clue += 1


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

        game.draw_top_panel()
        game.draw_cells()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()