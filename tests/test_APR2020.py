import unittest
from APR2020.RemoveOneLayerofParenthesis import remove_outermost_parenthesis
from APR2020.IndexofLargerNextNumber import larger_number
from APR2020.DuplicateSubtrees import dup_trees, Node as dNode
from APR2020.SplitaBinarySearchTree import split_bst, Node as sNode

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

    def test_split_bst(self):
        n2 = sNode(2)
        n1 = sNode(1, None, n2)

        n5 = sNode(5)
        n4 = sNode(4, None, n5)

        root = sNode(3, n1, n4)



        # (3, (1, (2)), (4, None, (5)))
        # How the tree looks like
        #     3
        #   /   \
        #  1     4
        #   \     \
        #    2     5

        tu = split_bst(root, 2)
        self.assertEqual(['(1, None, (2))', '(3, None, (4, None, (5)))'], list(map(lambda x: str(x), tu)))

        # ((1, None, (2)), (3, None, (4, None, (5))))
        # Split into two trees
        # 1    And   3
        #  \          \
        #   2          4
        #               \
        #                5

        n3 = sNode(3)
        n2 = sNode(2, None, n3)
        n1 = sNode(1, None, n2)

        n6 = sNode(6)
        n5 = sNode(5, None, n6)

        root = sNode(4, n1, n5)

        tu = split_bst(root, 2)
        self.assertEqual([ '(1, None, (2))', '(4, (3), (5, None, (6)))'], list(map(lambda x: str(x), tu)))