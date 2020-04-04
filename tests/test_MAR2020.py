import unittest
from MAR2020.MazeProblem import paths_through_maze
from MAR2020.FilterBinaryTreeLeaves import filter, Node as fNode
from MAR2020.SwapEveryTwoNodesinaLinkedList import swap_every_two , Node as sNode
from MAR2020.MakingChange import make_change
from MAR2020.PhoneNumbers import makeWords as phoneNumberMarkWords
from MAR2020.LargestPathSumfromRootToLeaf import largest_path_sum, Node as lNode
from MAR2020.DetermineIfNumber import parse_number
from MAR2020.PickingupChange import max_change
from MAR2020.FindSubtree import find_subtree, Node as fSubNode
from MAR2020.SwapBits import swap_bits
from MAR2020.Anagramsinastring import find_anagrams
from MAR2020.SumofSquares import square_sum

class Mar2020Suite(unittest.TestCase):
    def test_paths_through_maze(self):
        self.assertEqual(2, paths_through_maze([[0, 1, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]]))
        self.assertEqual(3, paths_through_maze([[0, 0, 0],
                                  [0, 0, 1],
                                  [0, 0, 0]]))

    def test_filterBinaryTreeLeave(self):
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

    def test_phoneNumbers(self):
        self.assertEqual(['dog', 'fog'], phoneNumberMarkWords('364'))
        self.assertEqual(['fish'], phoneNumberMarkWords('3474'))

    def test_largest_path_sum(self):
        tree = lNode(1)
        tree.left = lNode(3)
        tree.right = lNode(2)
        tree.right.left = lNode(4)
        tree.left.right = lNode(5)
        #    1
        #  /   \
        # 3     2
        #  \   /
        #   5 4
        self.assertEqual([1, 3, 5],largest_path_sum(tree))
        # [1, 3, 5]

        tree = lNode(1)
        tree.left = lNode(3)
        tree.right = lNode(2)
        tree.right.left = lNode(4)
        tree.left.right = lNode(5)
        tree.left.right.left = lNode(6)
        tree.left.left = lNode(20)
        print(largest_path_sum(tree))
        self.assertEqual([1, 3, 20], largest_path_sum(tree))

    def test_parseNumber(self):
        self.assertTrue(parse_number("-12e2"))
        # True

        self.assertFalse(parse_number("-1.5.1e2"))
        # False

        self.assertFalse(parse_number("-1.5e1.55"))
        # False

        self.assertTrue(parse_number("-1.5e5"))
        # True

        self.assertFalse(parse_number("1e1.2"))
        # False

        self.assertFalse(parse_number("1 2"))
        # False

        self.assertTrue(parse_number("1.5e5"))
        # True

        self.assertTrue(parse_number("-.3"))
        # True

        self.assertTrue(parse_number("-123"))
        # True

        self.assertFalse(parse_number("12a"))
        # False

        self.assertTrue(parse_number("12.3"))
        # True

    def test_max_change(self):
        mat = [
            [0, 3, 0, 2],
            [1, 2, 3, 3],
            [6, 0, 3, 2]
        ]
        self.assertEqual(13, max_change(mat))

    def test_find_subtree(self):
        t3 = fSubNode(4, fSubNode(3), fSubNode(2))
        t2 = fSubNode(5, fSubNode(4), fSubNode(-1))
        t = fSubNode(1, t2, t3)

        s = fSubNode(4, fSubNode(3), fSubNode(1))
        self.assertFalse(find_subtree(s, t))

        s = fSubNode(4, fSubNode(3), fSubNode(2))
        #"""
        #Tree t:
        #    1
        #   / \
        #  4   5
        # / \ / \
        #3  2 4 -1
    
        #Tree s:
        #  4
        # / \
        #3  2
        #"""

        self.assertTrue(find_subtree(s, t))
        # True

    def test_swap_bits(self):
        self.assertEqual("0b01010101010101010101010101010101",f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
        # 0b01010101010101010101010101010101
        self.assertEqual("0b00000000000000000000000000111010", f"0b{swap_bits(0b110101):032b}")

    def test_find_anagrams(self):
        self.assertEqual([3, 7],find_anagrams('acdbacdacb', 'abc'))

    def test_square_sum(self):
        self.assertEqual(2, square_sum(13))
        # Min sum is 3^2 + 2^2
        # 2

        self.assertEqual(2, square_sum(125))