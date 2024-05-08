from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(1000, 1000)
    cell = Cell(10, 10, 50, 50, win)
    cell2 = Cell(70, 70, 110, 110, win)
    cell.draw("black")
    cell2.draw("black")
    cell.draw_move(cell2)
    cell.draw_move(cell2, True)
    win.wait_for_close()


if __name__ == "__main__":
    main()