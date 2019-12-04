from DEC2019.TrappingRainwater import capacity as trapwatercapacity
from DEC2019.BuddyStrings import Solution as buddyStringSolu
from DEC2019.DeepestNodeinaBinaryTree import deepest as DeepestNodeBTree, Node as BNode
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