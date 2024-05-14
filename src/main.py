from window import Window
from line import Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(1000, 1000)
    maze = Maze(50, 50, 10, 30, 20, 20, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()