from .context import NOV2019
from NOV2019.TwoSum import two_sum, two_sum_HashSet
from NOV2019.SingleNumber import singleNumber
from NOV2019.NondecreasingArraywithSingleModification import Solution as NAS
from NOV2019.Floor_and_Ceiling_of_a_Binary_Search_Tree import findCeilingFloor as BinaryTreeFindCeilingFloor
from NOV2019.Floor_and_Ceiling_of_a_Binary_Search_Tree import Node as BinaryTreeNode
from NOV2019.InvertaBinaryTree import Node as BNode
from NOV2019.InvertaBinaryTree import invert as invertBTree
import unittest


class NOV2019Suite(unittest.TestCase):
    """Basic test cases."""

    def test_TwoSum(self):
        self.assertTrue(two_sum([4, 7, 1, -3, 2], 5))
        self.assertFalse(two_sum([4, 7, 1, -3, 2], 10))
        self.assertTrue(two_sum([4, 7, 2, -3, 2], 4))
        self.assertTrue(two_sum([4, 7, 2, -3, 2, 93], 90))

        self.assertTrue(two_sum_HashSet([4, 7, 2, -3, 2, 93], 90))
        self.assertTrue(two_sum_HashSet([4, 7, 1, -3, 2], 5))
        self.assertFalse(two_sum_HashSet([4, 7, 1, -3, 2], 10))
        self.assertTrue(two_sum_HashSet([4, 7, 2, -3, 2], 4))

    def testSingleNumber(self):
        r = singleNumber([4, 3, 2, 4, 1, 3, 2])
        self.assertIn(1, r)
        r = singleNumber([10,4, 3, 2, 4, 1, 3, 2])
        self.assertIn(10, r)
        self.assertIn(1, r)
        r = singleNumber([ 4, 3, 2, 4, 3, 2, 1])
        self.assertIn(1, r)

    def testNondecreasingArraywithSingleModification(self):
        solu = NAS()
        self.assertTrue(solu.check([13, 4, 7]))
        self.assertFalse(solu.check([5,1,3,2,5]))

    def testFloor_and_Ceiling_of_a_Binary_Search_Tree(self):
        root = BinaryTreeNode(8)
        root.left = BinaryTreeNode(4)
        root.right = BinaryTreeNode(12)

        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(6)

        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(14)

        self.assertEqual( BinaryTreeFindCeilingFloor(root, 5), (4,6) )
        self.assertEqual(BinaryTreeFindCeilingFloor(root, 11), (10, 12))

    def testInvertBTree(self):
        root = BNode('a')
        root.left = BNode('b')
        root.right = BNode('c')
        root.left.left = BNode('d')
        root.left.right = BNode('e')
        root.right.left = BNode('f')

        outPutlst = []
        root.preorderOut(outPutlst)
        self.assertEqual(outPutlst, ['a', 'b', 'd', 'e', 'c', 'f'])
        # a b d e c f
        outPutlst.clear()
        invertBTree(root)
        root.preorderOut(outPutlst)
        self.assertEqual(outPutlst, ['a', 'c', 'f', 'b', 'e', 'd'])
        # a c f b e d