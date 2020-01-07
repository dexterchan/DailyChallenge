from Jan2020.FullBinaryTree import fullBinaryTree, Node as fNode
from Jan2020.DecodeString import decodeString
from Jan2020.CircleOfChainedWords import chainedWords
from Jan2020.JumpToTheEnd import jumpToEnd
from Jan2020.H_Index import hIndex

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