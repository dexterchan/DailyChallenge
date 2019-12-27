from DEC2019.TrappingRainwater import capacity as trapwatercapacity
from DEC2019.BuddyStrings import Solution as buddyStringSolu
from DEC2019.DeepestNodeinaBinaryTree import deepest as DeepestNodeBTree, Node as BNode
from DEC2019.FirstMissingPositiveInteger import first_missing_positive
from DEC2019.ValidateBinarySearchTree import is_bst, TreeNode as TNode
from DEC2019.GetallValuesataCertainHeightinaBinaryTree import valuesAtHeight, Node as HNode
from DEC2019.LongestSubstringWithKDistinctCharacters import longest_substring_with_k_distinct_characters
from DEC2019.CountNumberofUnivalSubtrees import count_unival_subtrees, Node as UNode
from DEC2019.ReconstrunctBinaryTreefromPreorderandInorderTraversals import reconstruct, Node as RNode
from DEC2019.ThreeSum import Solution_Sort as ThreeSumSolution
from DEC2019.LargestBSTinaBinaryTree import largest_bst_subtree, TreeNode as tNode
from DEC2019.GroupWordsthatareAnagrams import groupAnagramWords
from DEC2019.MinimumRemovalsforValidParenthesis import count_invalid_parenthesis
from DEC2019.RunningMedian import running_median
from DEC2019.SortColors import ConstantSolution as SortColorSolution
from DEC2019.WordOrderinginaDifferentAlphabeticalOrder import isSorted
from DEC2019.MergeListOfNumberIntoRanges import findRanges
from DEC2019.ArithmeticBinaryTree import evaluate as evaulateBFS, Node as ANode
import unittest
import functools

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

    def test_valuesAtHeight(self):
        a = HNode(1)
        a.left = HNode(2)
        a.right = HNode(3)
        a.left.left = HNode(4)
        a.left.right = HNode(5)
        a.right.right = HNode(7)
        self.assertEqual(valuesAtHeight(a, 3), [4,5,7])
        # [4, 5, 7]

        a = HNode(1)
        a.left = HNode(2)
        a.right = HNode(3)
        a.left.left = HNode(4)
        a.left.right = HNode(5)
        a.right.right = HNode(7)
        self.assertEqual(valuesAtHeight(a, 2), [2,3])

    def test_longest_substring_with_k_distinct_characters(self):
        self.assertEqual(longest_substring_with_k_distinct_characters('aabcdefff', 3), 5)

    def test_count_unival_subtrees(self):
        a = UNode(0)
        a.left = UNode(1)
        a.right = UNode(1)
        a.right.left = UNode(1)
        a.right.left.left = UNode(1)
        a.right.left.right = UNode(1)
        #   0
        #  / \
        # 1   1
        #    /
        #   1
        #  / \
        # 1   1
        self.assertEqual(count_unival_subtrees(a), 5)
        # 5

        a = UNode(0)
        a.left = UNode(1)
        a.right = UNode(1)
        a.right.left = UNode(1)
        a.right.right = UNode(0)
        a.right.left.left = UNode(1)
        a.right.left.right = UNode(1)
        #   0
        #  / \
        # 1   1
        #    / \
        #   1   0
        #  / \
        # 1   1
        self.assertEqual(count_unival_subtrees(a), 5)
        # 5

        a = UNode(0)
        a.left = UNode(1)
        a.right = UNode(0)
        a.right.left = UNode(1)
        a.right.right = UNode(0)
        a.right.left.left = UNode(1)
        a.right.left.right = UNode(1)

        #   0
        #  / \
        # 1   0
        #    / \
        #   1   0
        #  / \
        # 1   1
        self.assertEqual(count_unival_subtrees(a),5)
        # 5

        a = UNode(0)
        a.left = UNode(1)
        a.right = UNode(1)
        a.right.left = UNode(1)
        a.right.right = UNode(1)
        a.right.left.left = UNode(1)
        a.right.left.right = UNode(1)

        #   0
        #  / \
        # 1   1
        #    / \
        #   1   1
        #  / \
        # 1   1
        self.assertEqual(count_unival_subtrees(a), 6)
        # 6
    def test_reconstruct(self):
        tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                           ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
        self.assertEqual(str(tree), 'abcdefg')

        tree = reconstruct(list('bdeij'), list('dbiej'))
        self.assertEqual(str(tree),'bdeij')

        tree = reconstruct(list('abdeijcfg'), list('dbiejafcg'))
        self.assertEqual(str(tree),'abcdefgij')


    def test_ThreeSumSolution(self):
        nums = [1, -2, 1, 0, 5]
        r = (ThreeSumSolution().threeSum(nums))
        self.assertEqual(len(r), 1)
        for array in r:
            self.assertEqual( functools.reduce(lambda a,b: a+b, array ), 0 )

        # [[-2, 1, 1]]

        nums = [0, -1, 2, -3, 1]
        r = (ThreeSumSolution().threeSum(nums))
        self.assertEqual(len(r), 2)
        for array in r:
            self.assertEqual( functools.reduce(lambda a,b: a+b, array ), 0 )


    def test_largest_bst_subtree(self):
        #     5
        #    / \
        #   6   7
        node = tNode(5)
        node.left = tNode(6)
        node.right = tNode(7)
        t = largest_bst_subtree(node)
        self.assertEqual(str(t), "6")
        # 749

        #     5
        #    / \
        #   6   7
        #  /   / \
        # 2   4   9
        node = tNode(5)
        node.left = tNode(6)
        node.right = tNode(7)
        node.left.left = tNode(2)
        node.right.left = tNode(4)
        node.right.right = tNode(9)
        t = largest_bst_subtree(node)
        self.assertEqual(str(t), "749")

        #     5
        #    / \
        #   3   7
        #  /   / \
        # 2   4   9
        node = tNode(5)
        node.left = tNode(3)
        node.right = tNode(7)
        node.left.left = tNode(2)
        node.right.left = tNode(4)
        node.right.right = tNode(9)
        t = largest_bst_subtree(node)
        self.assertEqual(str(t), "532749")

    def test_groupAnagramWords(self):
        result = groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg'])

        self.assertIn(['abc', 'cba'], result)
        self.assertIn(['efg'], result)
        self.assertIn(['bcd', 'cbd'], result)

    def test_count_invalid_parenthesis(self):
        self.assertEqual(count_invalid_parenthesis("()())()"),1)
        # 1

        self.assertEqual(count_invalid_parenthesis("()"),0)
        # 0

        self.assertEqual(count_invalid_parenthesis("((()())()"), 1)
        # 1

        self.assertEqual(count_invalid_parenthesis(")()("), 2)
        # 0

    def test_running_median(self):
        m = running_median([2, 1, 4, 7, 2, 0, 5])
        self.assertEqual(m, [2, 1.5, 2, 3.0, 2, 2.0, 2])

    def test_SortColorSolution(self):
        nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
        SortColorSolution().sortColors(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2])

        nums = [0, 2, 1, 0, 1, 2]
        SortColorSolution().sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])

    def test_isSorted(self):
        self.assertFalse(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
        # False
        self.assertTrue(isSorted(["zyx", "zyxw", "zyxwy"],
                       "zyxwvutsrqponmlkjihgfedcba"))

    def test_findRanges(self):
        self.assertEqual(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]), ['0-2', '5-5', '7-11', '15-15'])
        # ['0->2', '5->5', '7->11', '15->15']

        self.assertEqual(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 12]), ['0-2', '5-5', '7-12'])
        # ['0->2', '5->5', '7->12']

    def test_evaulateBFS(self):
        PLUS = "+"
        MINUS = "-"
        TIMES = "*"
        DIVIDE = "/"

        tree = ANode(TIMES)
        tree.left = ANode(PLUS)
        tree.left.left = ANode(3)
        tree.left.right = ANode(2)
        tree.right = ANode(PLUS)
        tree.right.left = ANode(4)
        tree.right.right = ANode(5)

        self.assertEqual(evaulateBFS(tree), 45)