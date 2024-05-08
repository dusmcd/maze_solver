from window import Window
from line import Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(1000, 1000)
    Maze(50, 50, 10, 10, 40, 40, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()