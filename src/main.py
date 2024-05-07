from window import Window
from line import Line, Point

def main():
    win = Window(1000, 1000)
    line = Line(Point(100, 100), Point(200, 200))
    line2 = Line(Point(80, 600), Point(95, 12))
    win.draw_line(line, "red")
    win.draw_line(line2, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()