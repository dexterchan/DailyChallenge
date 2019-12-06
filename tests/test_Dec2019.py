from DEC2019.TrappingRainwater import capacity as trapwatercapacity
from DEC2019.BuddyStrings import Solution as buddyStringSolu
from DEC2019.DeepestNodeinaBinaryTree import deepest as DeepestNodeBTree, Node as BNode
from DEC2019.FirstMissingPositiveInteger import first_missing_positive
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