import unittest
from MAR2020.MazeProblem import paths_through_maze
from MAR2020.FilterBinaryTreeLeaves import filter, Node as fNode
from MAR2020.SwapEveryTwoNodesinaLinkedList import swap_every_two , Node as sNode
from MAR2020.MakingChange import make_change

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

    def test_swap_every_two(self):
        llist = sNode(1, sNode(2, sNode(3, sNode(4, sNode(5)))))
        self.assertEqual("2, (1, (4, (3, (5, (None)))))",str(swap_every_two(llist)))
        # 2, (1, (4, (3, (5, (None)))))

        llist = sNode(1, sNode(2))
        self.assertEqual("2, (1, (None))", str(swap_every_two(llist)))

    def test_make_change(self):
        self.assertEqual("3 coins (25+10+1)",make_change([1, 5, 10, 25], 36))
        # 3 coins (25 + 10 + 1)

        self.assertEqual("2 coins (25+5)",make_change([1, 5, 10, 25], 30))
        # 2 coins (25 + 5)

        self.assertEqual("3 coins (25+1+1)",make_change([1, 5, 10, 25], 27))
