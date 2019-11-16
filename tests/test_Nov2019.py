from .context import NOV2019
from NOV2019.TwoSum import two_sum, two_sum_HashSet
from NOV2019.SingleNumber import singleNumber
from NOV2019.NondecreasingArraywithSingleModification import Solution as NAS
from NOV2019.Floor_and_Ceiling_of_a_Binary_Search_Tree import findCeilingFloor as BinaryTreeFindCeilingFloor
from NOV2019.Floor_and_Ceiling_of_a_Binary_Search_Tree import Node as BinaryTreeNode
from NOV2019.InvertaBinaryTree import Node as BNode
from NOV2019.InvertaBinaryTree import invert as invertBTree
from NOV2019.MaximumInAStack import MaxStack as MaxStack
from NOV2019.NumberofWaystoClimbStairs import staircase, staircase_brutal_force
from NOV2019.FindPythagoreanTriplets import findPythagoreanTriplets_nSquare
from NOV2019.CreateaSimpleCalculator import eval
from NOV2019.LongestSequencewithTwoUniqueNumbers import findSequence as longSeq2UniqueNumber
from NOV2019.FindCyclesinaGraph import find_cycle as findCycicGraph
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
        r = singleNumber([10, 4, 3, 2, 4, 1, 3, 2])
        self.assertIn(10, r)
        self.assertIn(1, r)
        r = singleNumber([4, 3, 2, 4, 3, 2, 1])
        self.assertIn(1, r)

    def testNondecreasingArraywithSingleModification(self):
        solu = NAS()
        self.assertTrue(solu.check([13, 4, 7]))
        self.assertFalse(solu.check([5, 1, 3, 2, 5]))

    def testFloor_and_Ceiling_of_a_Binary_Search_Tree(self):
        root = BinaryTreeNode(8)
        root.left = BinaryTreeNode(4)
        root.right = BinaryTreeNode(12)

        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(6)

        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(14)

        self.assertEqual( BinaryTreeFindCeilingFloor(root, 5), (4, 6))
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

    def testMaxStack(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertEqual(s.max(), 3)
        # 3
        s.pop()
        s.pop()
        # 2
        self.assertEqual(s.max(), 2)

        s = MaxStack()
        s.push(100)
        s.push(20)
        s.push(50)
        self.assertEqual(s.max(), 100)
        s.push(100)
        self.assertEqual(s.max(), 100)
        self.assertEqual(s.pop(), 100)
        self.assertEqual(s.max(), 100)
        s.push(150)
        self.assertEqual(s.max(), 150)
        s.push(200)
        self.assertEqual(s.max(), 200)
        s.push(50)
        self.assertEqual(s.max(), 200)
        s.push(150)
        self.assertEqual(s.max(), 200)
        s.push(200)
        self.assertEqual(s.max(), 200)

        self.assertEqual(s.pop(), 200)
        self.assertEqual(s.max(), 200)
        self.assertEqual(s.pop(), 150)
        self.assertEqual(s.pop(), 50)
        self.assertEqual(s.max(), 200)
        self.assertEqual(s.pop(), 200)
        self.assertEqual(s.max(), 150)
        self.assertEqual(s.pop(), 150)
        self.assertEqual(s.max(), 100)
        self.assertEqual(s.pop(), 50)
        self.assertEqual(s.max(), 100)

    def testStairs(self):
        self.assertEqual(staircase_brutal_force(4), 5)
        self.assertEqual(staircase_brutal_force(5), 8)
        for n in range(7, 10):
            self.assertEqual(staircase_brutal_force(n), staircase(n))

    def testfindPythagoreanTriplets_nSquare(self):
        self.assertTrue(findPythagoreanTriplets_nSquare(  [3, 5, 12, 5, 13]))

        self.assertFalse(findPythagoreanTriplets_nSquare([3, 5, 12, 5, 12]))

    def testEval(self):
        self.assertEqual(eval('2+(3+5)'), 10)
        self.assertEqual(eval('2+(3+5)+1'), 11)

        self.assertEqual(eval('2+(3+5+(2-3))+1'), 10)
        self.assertEqual(eval('-2+3'), 1)
        self.assertEqual(eval('-(2+3)'), -5)
        self.assertEqual(eval('- (3 + ( 2 - 1 ) )'), -4)

    def testlongSeq2UniqueNumber(self):
        self.assertEqual (longSeq2UniqueNumber([1, 3, 5, 3, 1, 3, 1, 5]), 4)
        self.assertEqual(longSeq2UniqueNumber([1, 3, 0, 1, 1, 3, 1, 5]), 4)
        self.assertEqual(longSeq2UniqueNumber([1, 3, 3, 1, 1, 3, 1, 5]), 7)

    def testFindCycicGraph(self):
        graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        self.assertFalse(findCycicGraph(graph))
        graph['c'] = graph
        self.assertTrue(findCycicGraph(graph))