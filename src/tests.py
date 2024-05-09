import unittest
from maze import Maze

test_cases = [
    (Maze(0, 0, 10, 10, 15, 15), (10, 10)),
    (Maze(5, 5, 12, 6, 4, 6), (12, 6)),
    (Maze(45, 45, 1, 1, 1, 1), (1, 1)),
    (Maze(2, 2, 11, 13, 10, 10), (11, 13))
]
class MazeTest(unittest.TestCase):
    def test_create_cells(self):
        for test_case in test_cases:
            maze = test_case[0]
            expected_rows = test_case[1][0]
            expected_cols = test_case[1][1]
            cells = maze.get_cells()
            self.assertEqual(expected_cols, len(cells[0]))
            self.assertEqual(expected_rows, len(cells))


if __name__ == "__main__":
    unittest.main()