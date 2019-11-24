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
from NOV2019.WordSearch import word_search
from NOV2019.MinimumSizeSubarraySum import Solution as MinSizeSubArray
from NOV2019.IntersectionLinkedList import intersection as intersectionLinkedList
from NOV2019.IntersectionLinkedList import Node as INode
from NOV2019.FindCyclesinaGraph import find_cycle as findCycicGraph
from NOV2019.FallingDominoes import Solution as Dominos
from NOV2019.RemoveConsecutiveNodesthatSumto0 import removeConsecutiveSumTo0
from NOV2019.RemoveConsecutiveNodesthatSumto0 import Node as CNode
from NOV2019.Removek_thLastElementFromLinkedList import remove_kth_from_linked_list
from NOV2019.Removek_thLastElementFromLinkedList import Node as RNode
from NOV2019.WitnessofTheTallPeople import witnesses
from NOV2019.CoursePrerequisites import courses_to_take
from NOV2019.MoveZeros import Solution as MoveZeros
from NOV2019.FindthekthLargestElementinaList import findKthLargest
from NOV2019.SpiralTraversalofGrid import  matrix_spiral_print

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


    def testword_search(self):
        matrix = [
            ['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']]
        self.assertTrue(word_search(matrix, 'FOAM'))
        self.assertTrue(word_search(matrix, 'MASS'))

    def testMinSizeSUbArray(self):
        solu = MinSizeSubArray()
        self.assertEqual(solu.minSubArrayLen([2, 3, 1, 2, 4, 3], 7), 2)

        self.assertEqual(solu.minSubArrayLen([2, 3, 1, 2, 4, 3], 4), 1)

        self.assertTrue(solu.minSubArrayLen([8, 3, 5, 2, 1, 10], 8), 1)

    def testIntersectionLinkedList(self):
        a = INode(1)
        a.next = INode(2)
        a.next.next = INode(3)
        a.next.next.next = INode(4)
        b = INode(6)
        b.next = a.next.next
        c = intersectionLinkedList(a, b)
        self.assertEqual(c.toString(), "[3, 4]")

    def testFindCycicGraph(self):
        graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        self.assertFalse(findCycicGraph(graph))
        graph['c'] = graph
        self.assertTrue(findCycicGraph(graph))

    def testDominos(self):
        result = (Dominos().pushDominoes('..R...L..R.'))
        self.assertEqual(result, "..RR.LL..RR")

        result = (Dominos().pushDominoes('R.L...L..R.'))
        self.assertEqual(result, "R.LLLLL..RR")

    def testRemoveConsecutiveNodesthatSumto0(self):
        node = CNode(10)
        node.next = CNode(5)
        node.next.next = CNode(-3)
        node.next.next.next = CNode(-3)
        node.next.next.next.next = CNode(1)
        node.next.next.next.next.next = CNode(4)
        node.next.next.next.next.next.next = CNode(-4)
        node = removeConsecutiveSumTo0(node)
        c = []
        while node:
            c.append(node.value)
            node = node.next
        self.assertEqual(c, [10])

        node = CNode(5)
        node.next = CNode(-3)
        node.next.next = CNode(-3)
        node.next.next.next = CNode(1)
        node.next.next.next.next = CNode(20)
        node.next.next.next.next.next = CNode(4)
        node.next.next.next.next.next.next = CNode(-4)
        node = removeConsecutiveSumTo0(node)
        c = []
        while node:
            c.append(node.value)
            node = node.next
        self.assertEqual(c, [20])

    def testRemovek_thLastElementFromLinkedList(self):
        head = RNode(1, RNode(2, RNode(3, RNode(4, RNode(5)))))
        head = remove_kth_from_linked_list(head, 1)
        self.assertEqual(str(head), "[1, 2, 3, 4]")


        head = RNode(1, RNode(2, RNode(3, RNode(4, RNode(5)))))
        head = remove_kth_from_linked_list(head, 3)
        self.assertEqual(str(head), "[1, 2, 4, 5]")

        head = RNode(1, RNode(2, RNode(3)))
        head = remove_kth_from_linked_list(head, 3)
        self.assertEqual(str(head), "[2, 3]")

    def testWitnesses(self):
        self.assertEqual(witnesses([3, 6, 3, 4, 1]),3)

    def courses_to_take(self):
        courses = {
            'CSC300': ['CSC100', 'CSC200'],
            'CSC200': ['CSC100'],
            'CSC100': []
        }
        c = courses_to_take(courses)
        self.assertEqual(c, ['CSC100', 'CSC200', 'CSC300'])

        courses = {
            'CSC300': ['CSC100', 'CSC200'],
            'CSC200': ['CSC100']
        }
        c = courses_to_take(courses)
        self.assertEqual(c, None)

        courses = {
            'CSC100': [],
            'CSC300': ['CSC100', 'CSC200'],
            'CSC200': ['CSC100']

        }
        c = courses_to_take(courses)
        self.assertEqual(c, ['CSC100', 'CSC200', 'CSC300'])

        courses = {
            'CSC100': [],
            'CSC300': ['CSC100', 'CSC200', 'ELE100'],
            'CSC200': ['CSC100']

        }
        c = courses_to_take(courses)
        self.assertEqual(c, None)

    def testMoveZeros(self):
        nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
        MoveZeros().moveZeros(nums)
        self.assertEqual(nums, [2,1,3,4,0,0,0,0,0,0])

    def testfindKthLargest(self):
        nums = [3, 5, 2, 4, 6, 8]
        res = findKthLargest(nums, 3)
        self.assertEqual(res, 5)
        res = findKthLargest(nums, 2)
        self.assertEqual(res, 6)

    def testmatrix_spiral_print(self):
        grid = [[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]]

        l = matrix_spiral_print(grid)
        self.assertEqual(l, [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12])