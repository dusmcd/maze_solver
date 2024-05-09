from line import Line, Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.center = ((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
    
    def draw(self, fill_color):
        top_left = (self.__x1, self.__y1)
        bottom_right = (self.__x2, self.__y2)
        top_right = (self.__x2, self.__y1)
        bottom_left = (self.__x1, self.__y2)

        left = Line(Point(top_left[0], top_left[1]), Point(bottom_left[0], bottom_left[1]))
        top = Line(Point(top_left[0], top_left[1]), Point(top_right[0], top_right[1]))
        right = Line(Point(top_right[0], top_right[1]), Point(bottom_right[0], bottom_right[1]))
        bottom = Line(Point(bottom_right[0], bottom_right[1]), Point(bottom_left[0], bottom_left[1]))


        if self.has_left_wall:
            self.__win.draw_line(left, fill_color)
        else:
            self.__win.draw_line(left, "#d9d9d9")
        if self.has_top_wall:
            self.__win.draw_line(top, fill_color)
        else:
            self.__win.draw_line(top, "#d9d9d9")
        if self.has_right_wall:
            self.__win.draw_line(right, fill_color)
        else:
            self.__win.draw_line(right, "#d9d9d9")
        if self.has_bottom_wall:
            self.__win.draw_line(bottom, fill_color)
        else:
            self.__win.draw_line(bottom, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        line = Line(Point(self.center[0], self.center[1]), Point(to_cell.center[0], to_cell.center[1]))
        fill_color = "red" if not undo else "gray"
        self.__win.draw_line(line, fill_color)