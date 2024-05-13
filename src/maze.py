from cell import Cell
import time
import random
import math

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for row in range(self.__num_rows):
            column = []
            for col in range(self.__num_cols):
                cell = self.__draw_cell(row, col)
                column.append(cell)
            self.__cells.append(column)

    def __draw_cell(self, i, j):
        maze_start = (self.__x1, self.__y1)
        top_left = (maze_start[0] + j * self.__cell_size_x,
                     maze_start[1] + i * self.__cell_size_y
                    )
        bottom_right = (maze_start[0] + j * self.__cell_size_x + self.__cell_size_x,
                         maze_start[1] + i * self.__cell_size_y + self.__cell_size_y
                        )
        cell = Cell(top_left[0], top_left[1], bottom_right[0], bottom_right[1], self.__win)
        if self.__win:
            cell.draw("black")
            self.__animate()
        return cell

    def __animate(self):
        if self.__win:
            self.__win.redraw()
        time.sleep(0.05)

    def get_cells(self):
        return self.__cells
    
    def get_num_cols(self):
        return self.__num_cols
    
    def get_num_rows(self):
        return self.__num_rows

    def __break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        exit = self.__cells[self.__num_rows - 1][self.__num_cols - 1]
        entrance.has_left_wall = False
        exit.has_right_wall = False
        if self.__win:
            entrance.draw("black")
            exit.draw("black")


    def __break_walls_r(self, i, j):
        current_cell = self.__cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = []
            if j + 1 < self.__num_cols and not self.__cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            if j - 1 > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if i + 1 < self.__num_rows and not self.__cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if i - 1 > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            
            if len(possible_directions) == 0:
                if self.__win:
                    current_cell.draw("black")
                return
            direction = math.floor(random.random() * len(possible_directions))
            next_cell = self.__cells[possible_directions[direction][0]][possible_directions[direction][1]]

            if possible_directions[direction][0] < i:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif possible_directions[direction][0] > i:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif possible_directions[direction][1] < j:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            else:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            if self.__win:
                current_cell.draw("black")
                next_cell.draw("black")
                self.__animate()

            self.__break_walls_r(possible_directions[direction][0], possible_directions[direction][1])
    
    def __reset_cells_visited(self):
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                self.__cells[row][col].visited = False