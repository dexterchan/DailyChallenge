import unittest
from APR2020.RemoveOneLayerofParenthesis import remove_outermost_parenthesis
from APR2020.IndexofLargerNextNumber import larger_number
from APR2020.DuplicateSubtrees import dup_trees, Node as dNode

class Apr2020Suite(unittest.TestCase):
    def test_remove_outermost_parenthesis(self):
        self.assertEqual("()()",remove_outermost_parenthesis('(()())'))
        # ()()

        self.assertEqual("()",remove_outermost_parenthesis('(())()'))
        # ()

        self.assertEqual("",remove_outermost_parenthesis('()()()'))
        # ' '

    def test_larger_number(self):
        self.assertEqual([2, 2, 3, 4, -1, -1], larger_number([3, 2, 5, 6, 9, 8]))

    def test_dup_trees(self):
        n3_1 = dNode(3)
        n2_1 = dNode(2, n3_1)
        n3_2 = dNode(3)
        n2_2 = dNode(2, n3_2)
        n1 = dNode(1, n2_1, n2_2)
        # Looks like
        #     1
        #    / \
        #   2   2
        #  /   /
        # 3   3

        self.assertEqual([['(3)', '(3)'], ['(2, (3))', '(2, (3))']], dup_trees(n1))
        # [[(3), (3)], [(2, (3)), (2, (3))]]
        # There are two duplicate trees
        #
        #     2
        #    /
        #   3
        # and just the leaf
        #
        # 3