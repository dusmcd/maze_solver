from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for row in range(self.num_rows):
            column = []
            for col in range(self.num_cols):
                cell = self.__draw_cell(row, col)
                column.append(cell)
            self.__cells.append(column)

    def __draw_cell(self, i, j):
        maze_start = (self.x1, self.y1)
        top_left = (maze_start[0] + j * self.cell_size_x,
                     maze_start[1] + i * self.cell_size_y
                    )
        bottom_right = (maze_start[0] + j * self.cell_size_x + self.cell_size_x,
                         maze_start[1] + i * self.cell_size_y + self.cell_size_y
                        )
        cell = Cell(top_left[0], top_left[1], bottom_right[0], bottom_right[1], self.__win)
        cell.draw("black")
        self.__animate()
        return cell

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
