import unittest
from MAR2020.MazeProblem import paths_through_maze

class Mar2020Suite(unittest.TestCase):
    def test_paths_through_maze(self):
        self.assertEqual(2, paths_through_maze([[0, 1, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]]))
        self.assertEqual(3, paths_through_maze([[0, 0, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]]))