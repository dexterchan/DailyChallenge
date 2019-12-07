from DEC2019.TrappingRainwater import capacity as trapwatercapacity
from DEC2019.BuddyStrings import Solution as buddyStringSolu
from DEC2019.DeepestNodeinaBinaryTree import deepest as DeepestNodeBTree, Node as BNode
from DEC2019.FirstMissingPositiveInteger import first_missing_positive
from DEC2019.ValidateBinarySearchTree import is_bst, TreeNode as TNode
import unittest


class Dec2019Suite(unittest.TestCase):
    def test_trapwatercapacity(self):
        self.assertEqual(trapwatercapacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
    def test_buddyStringSolu(self):

        self.assertTrue(buddyStringSolu().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
        # True
        self.assertFalse(buddyStringSolu().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
        # False

        self.assertTrue(buddyStringSolu().buddyStrings('ab', 'ba'))
        # True

        self.assertTrue(buddyStringSolu().buddyStrings('aaa', 'aaa'))
        # True
    def test_DeepestNodeBTree(self):
        root = BNode('a')
        root.left = BNode('b')
        root.left.left = BNode('d')
        root.right = BNode('c')

        self.assertEqual(DeepestNodeBTree(root), (root.left.left,3))
        # (d, 3)

        root = BNode('a')
        root.left = BNode('b')
        root.left.left = BNode('d')
        root.right = BNode('c')
        root.right.left = BNode('e')
        root.right.left.right = BNode('f')
        root.right.left.right.left = BNode('g')
        self.assertEqual(DeepestNodeBTree(root), (root.right.left.right.left, 5))

    def test_first_missing_positive(self):
        self.assertEqual(first_missing_positive([8, 7, 2, 3, 4, 5, -1, 10, 6, 1]), 9)

        self.assertEqual(first_missing_positive([7, 2, 3, 4, 5, -1, 10, 6, 1]), 8)

        self.assertEqual(first_missing_positive([7, 2, 3, 4, 5, -1, 1]), 6)

        self.assertEqual(first_missing_positive([3, 4, -1, 1]), 2)

    def test_isbst(self):
        a = TNode(5)
        a.left = TNode(3)
        a.right = TNode(7)
        a.left.left = TNode(1)
        a.left.right = TNode(10)
        a.right.left = TNode(6)
        self.assertFalse(is_bst(a, False))

        a = TNode(5)
        a.left = TNode(3)
        a.right = TNode(7)
        a.left.left = TNode(1)
        a.left.right = TNode(2)
        a.right.left = TNode(6)
        self.assertFalse(is_bst(a, False))

        a = TNode(5)
        a.left = TNode(3)
        a.right = TNode(7)
        a.left.left = TNode(1)
        a.left.right = TNode(4)
        a.right.left = TNode(6)
        self.assertTrue(is_bst(a, False))

        a = TNode(5)
        a.left = TNode(3)
        a.right = TNode(7)
        a.left.left = TNode(1)
        a.left.right = TNode(10)
        a.right.left = TNode(6)
        a.left.right.left = TNode(4)
        self.assertFalse(is_bst(a, False))