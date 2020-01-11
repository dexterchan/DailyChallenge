from Jan2020.FullBinaryTree import fullBinaryTree, Node as fNode
from Jan2020.DecodeString import decodeString
from Jan2020.CircleOfChainedWords import chainedWords
from Jan2020.JumpToTheEnd import jumpToEnd
from Jan2020.H_Index import hIndex
from Jan2020.SymmetricKaryTree import is_symmetric as is_SubTree_Symmetric, Node as SNode
from Jan2020.MaxandMinwithLimitedComparisons import find_min_max
from Jan2020.Fibonacci import Solution as Fibonacci
from Jan2020.FindtheSingleElementinanArrayofDuplicates import Solution as FindSingleFromArrayOfDuplicate

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