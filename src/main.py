from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(1000, 1000)
    cell = Cell(100, 100, 200, 200, win)
    cell.draw("red")
    win.wait_for_close()


if __name__ == "__main__":
    main()