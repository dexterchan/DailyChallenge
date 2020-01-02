from Jan2020.FullBinaryTree import fullBinaryTree, Node as fNode

import unittest
import functools

class Jan2020Suite(unittest.TestCase):
    def test_fullBinaryTree(self):
        tree = fNode(1)
        tree.left = fNode(2)
        tree.right = fNode(3)
        tree.right.right = fNode(4)
        tree.right.left = fNode(9)
        tree.left.left = fNode(0)
        res = str(fullBinaryTree(tree))
        self.assertEqual(res, "1\n03\n94")

        tree = fNode(1)
        tree.left = fNode(2)
        tree.right = fNode(3)
        tree.right.left = fNode(9)
        tree.left.left = fNode(0)
        res = str(fullBinaryTree(tree))
        self.assertEqual(res, "1\n09")