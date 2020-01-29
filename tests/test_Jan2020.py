from Jan2020.FullBinaryTree import fullBinaryTree, Node as fNode
from Jan2020.DecodeString import decodeString
from Jan2020.CircleOfChainedWords import chainedWords
from Jan2020.JumpToTheEnd import jumpToEnd
from Jan2020.H_Index import hIndex
from Jan2020.SymmetricKaryTree import is_symmetric as is_SubTree_Symmetric, Node as SNode
from Jan2020.MaxandMinwithLimitedComparisons import find_min_max
from Jan2020.Fibonacci import Solution as Fibonacci
from Jan2020.FindtheSingleElementinanArrayofDuplicates import Solution as FindSingleFromArrayOfDuplicate
from Jan2020.ConvertRomanNumeralstoDecimal import Solution as RomanConversion
from Jan2020.NoAdjRepeatingCharacters import rearrangeString
from Jan2020.MaketheLargestNumber import largestNum
from Jan2020.SmallestNumberthatisnotaSumofaSubsetofList import findSmallest
from Jan2020.MaximumPathSuminBinaryTree import maxPathSum, Node as MNode
from Jan2020.LowestCommonAncestorof2NodesinBinaryTree import lowestCommonAncestor, TreeNode as LTNode
from Jan2020.BinaryTreeLevelwithMinimumSum import minimum_level_sum, Node as BTMNode
from Jan2020.PlusOne import Solution as PlusOneSolu
from Jan2020.TopKFrequentwords import Solution as TopKFreqWords

import unittest

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

    def test_decodeString(self):
        self.assertEqual(decodeString('2[a2[b]c]'), "abbcabbc")
        # abbcabbc

        self.assertEqual(decodeString('a2[a]2[b]'), "aaabb")

        self.assertEqual(decodeString('2[a2[b]c2[d]]'), "abbcddabbcdd")

    def test_chainedWords(self):
        self.assertTrue(chainedWords(['apple', 'area', 'eggs', 'snack', 'karat', 'tuna']))
        self.assertTrue(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))

    def test_jumpToEnd(self):
        self.assertEqual(3, jumpToEnd([3, 2, 4, 1, 1, 9, 3, 4]))

        self.assertEqual(2, jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))

    def test_hIndex(self):
        self.assertEqual(hIndex([5, 3, 3, 1, 0]), 3)
        self.assertEqual(hIndex([5, 3, 3, 1, 4, 4, 4, 0]), 4)

    def test_is_SubTree_Symmetric(self):
        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4)]
        tree.children[1].children = [SNode(4), SNode(9)]
        tree.children[0].children[0].children = [SNode(10)]
        tree.children[1].children[0].children = [SNode(10)]
        self.assertFalse(is_SubTree_Symmetric(tree))
        # False

        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4)]
        tree.children[1].children = [SNode(4), SNode(9), SNode(5)]
        tree.children[0].children[0].children = [SNode(10)]
        tree.children[1].children[1].children = [SNode(10)]
        self.assertFalse(is_SubTree_Symmetric(tree))
        # False

        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4)]
        tree.children[1].children = [SNode(4), SNode(9)]
        tree.children[0].children[0].children = [SNode(10)]
        tree.children[1].children[1].children = [SNode(10)]
        self.assertTrue(is_SubTree_Symmetric(tree))
        # True

        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4), SNode(1)]
        tree.children[1].children = [SNode(1), SNode(4), SNode(9)]
        self.assertTrue(is_SubTree_Symmetric(tree))
        # True

        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4), SNode(1)]
        tree.children[1].children = [SNode(1), SNode(4), SNode(9)]
        tree.children[0].children[0].children = [SNode(10)]
        tree.children[1].children[2].children = [SNode(10)]
        self.assertTrue(is_SubTree_Symmetric(tree))
        # True

        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4), SNode(1)]
        tree.children[1].children = [SNode(1), SNode(4), SNode(9)]
        tree.children[0].children[0].children = [SNode(10)]
        self.assertFalse(is_SubTree_Symmetric(tree))
        # False

        tree = SNode(4)
        tree.children = [SNode(3), SNode(3)]
        tree.children[0].children = [SNode(9), SNode(4), SNode(1)]
        tree.children[1].children = [SNode(1), SNode(4), SNode(4)]
        self.assertFalse(is_SubTree_Symmetric(tree))
        # False

    def test_find_min_max(self):
        self.assertEqual(find_min_max([3, 5, 1, 2, 4, 8]), (1,8))

    def test_Fibonacci(self):
        n = 9
        self.assertEqual(Fibonacci().fibonacci(n), 34)

    def test_FindSingleFromArrayOfDuplicate(self):
        nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
        self.assertEqual(3, FindSingleFromArrayOfDuplicate().findSingle(nums))

    def test_RomanConversion(self):
        n = 'MCMX'
        self.assertEqual(1910, RomanConversion().romanToInt(n))
        # 1910

        self.assertEqual(2910, RomanConversion().romanToInt('MMCMX'))
        # 2910

        self.assertEqual(2818, RomanConversion().romanToInt('MMCCMXIIX'))
        # 2918

    def test_rearrangeString(self):
        self.assertEqual("cbcacbc",rearrangeString('abbcccc'))
        # cbcacbc

        self.assertEqual("cbcabc",rearrangeString('abbccc'))
        # cbcabc

        self.assertIsNone(rearrangeString('abbccccc'))
        # None

    def test_largestNum(self):
        self.assertEqual(77245, largestNum([7, 45, 72]))

        self.assertEqual(982245, largestNum([9, 45, 822]))

        self.assertEqual(77245217,largestNum([17, 7, 2, 45, 72]))
        # 77245217

    def test_findSmallest(self):
        self.assertEqual(7, findSmallest([1, 2, 3, 8, 9, 10]))
        # 7

        self.assertIsNone(findSmallest([1, 2, 3, 4, 8, 9, 10]))
        # None

        self.assertEqual(23, findSmallest([1, 2, 3, 7, 9, 100]))
        # 23

    def test_maxPathSum(self):
        #       *10
        #       /  \
        #     *2   *10
        #     / \     \
        #   20  *100    25

        root = MNode(10)
        root.left = MNode(2)
        root.right = MNode(10)
        root.left.left = MNode(20)
        root.left.right = MNode(100)
        root.right.right = MNode(25)

        self.assertEqual(147, maxPathSum(root))
        # 147

        #       *10
        #       /  \
        #     *2   *10
        #     / \     \
        #   *20  1    -25
        #             /  \
        #            3    4
        root = MNode(10)
        root.left = MNode(2)
        root.right = MNode(10)
        root.left.left = MNode(20)
        root.left.right = MNode(1)
        root.right.right = MNode(-25)
        root.right.right.left = MNode(3)
        root.right.right.right = MNode(4)
        self.assertEqual(42, maxPathSum(root))
        # 42

        #       *10
        #       /  \
        #     -2   *10
        root = MNode(10)
        root.left = MNode(-2)
        root.right = MNode(10)
        self.assertEqual(20, maxPathSum(root))
        # 20

    def test_lowestCommonAncestor(self):
        root = LTNode('a')
        root.left = LTNode('b')
        root.left.parent = root
        root.right = LTNode('c')
        root.right.parent = root
        a = root.right.left = LTNode('d')
        root.right.left.parent = root.right
        b = root.right.right = LTNode('e')
        root.right.right.parent = root.right

        self.assertEqual('c', lowestCommonAncestor(root, a, b).val)

    def test_minimum_level_sum(self):
        #     10
        #    /  \
        #   2    8
        #  / \    \
        # 4   1    2
        node = BTMNode(10)
        node.left = BTMNode(2)
        node.right = BTMNode(8)
        node.left.left = BTMNode(4)
        node.left.right = BTMNode(1)
        node.right.right = BTMNode(2)

        self.assertEqual(7, minimum_level_sum(node))

    def test_PlusOneSolu(self):
        num = [2, 9, 9]
        self.assertEqual([3,0,0], PlusOneSolu().plusOne(num))
        # [3, 0, 0]
        num = [9, 9, 9]
        self.assertEqual([1,0,0,0], PlusOneSolu().plusOne(num))

    def test_TopKFreqWords(self):
        words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
        k = 2
        self.assertEqual(['pro', 'daily'], TopKFreqWords().topKFrequent(words, k))
        # ['pro', 'daily']

        words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems", "daily"]
        k = 2
        self.assertEqual(['daily', 'pro'], TopKFreqWords().topKFrequent(words, k))