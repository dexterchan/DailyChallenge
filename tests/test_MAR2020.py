import unittest
from MAR2020.MazeProblem import paths_through_maze
from MAR2020.FilterBinaryTreeLeaves import filter, Node as fNode

class Mar2020Suite(unittest.TestCase):
    def test_paths_through_maze(self):
        self.assertEqual(2, paths_through_maze([[0, 1, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]]))
        self.assertEqual(3, paths_through_maze([[0, 0, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]]))

    def test_fitler(self):
        n5 = fNode(2)
        n4 = fNode(1)
        n3 = fNode(1, n4)
        n2 = fNode(1, n5)
        n1 = fNode(1, n2, n3)
        self.assertEqual("value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)",str(filter(n1, 1)))
