from .context import OCT2019

from OCT2019.findLongestSubStringWithRepeatedCharacters import Solution2 as findLongestSubStringWithRepeatedCharacters
from OCT2019.LongestPalindromicSubstring import Solution as LPSS
from OCT2019.ValidateBalancedParentheses import Solution as BP
from OCT2019.FirstandLastIndicesofanElementinSortedArray import Solution as FLIESA
from OCT2019.ReverseAList import ListNode as ListNode

import unittest


class OCT2019Suite(unittest.TestCase):
    """Basic test cases."""

    def test_LongestSubStringWithRepeatedCharacters(self):
        solu = findLongestSubStringWithRepeatedCharacters()
        length = solu.lengthOfLongestSubstring("abrkaabcdefghijjxxx")
        self.assertEqual(length[0],10)

        solu = findLongestSubStringWithRepeatedCharacters()
        length = solu.lengthOfLongestSubstring("abcdddddfghjklmnbmhj")
        self.assertEqual(length[0], 10)

        solu = findLongestSubStringWithRepeatedCharacters()
        length = solu.lengthOfLongestSubstring("ABDEFGABEF")
        self.assertEqual(length[0], 6)



    def test_LPSS (self):
        solu = LPSS()
        ss = solu.longestPalindrome("tracecars")
        self.assertEqual(ss, "racecar")

        ss = solu.longestPalindrome("eggissimple")
        self.assertEqual(ss, "issi")

    def test_BalancedParentheses(self):
        solu = BP ()
        # Test Program
        s = "()(){(())"
        # should return False
        self.assertFalse(solu.isValid(s))

        s = ""
        # should return True
        self.assertTrue(solu.isValid(s))

        s = "([{}])()"
        # should return True
        self.assertTrue(solu.isValid(s))

        s = "([{}])())"
        # should return False
        self.assertFalse(solu.isValid(s))

        s = "([{}])("
        # should return False
        self.assertFalse(solu.isValid(s))

        s = "([{}])([])"
        # should return True
        self.assertTrue(solu.isValid(s))

    def testFLIESA(self):
        solu = FLIESA()

        # Test program
        arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
        x = 2
        ret = (solu.getRange(arr, x))
        self.assertEqual(ret, [1, 4])

        arr = [1, 2, 2, 2, 2]
        x = 2
        ret = (solu.getRange(arr, x))
        self.assertEqual(ret, [1, 4])


        arr = [1, 5]
        x = 2
        ret = (solu.getRange(arr, x))
        self.assertEqual(ret, [-1, -1])

    def testListNode(self):
        # Test Program
        # Initialize the test list:
        testHead = ListNode(4)
        node1 = ListNode(3)
        testHead.next = node1
        node2 = ListNode(2)
        node1.next = node2
        node3 = ListNode(1)
        node2.next = node3
        testTail = ListNode(0)
        node3.next = testTail


        testHead.reverseIteratively(testHead)

        currentNode = testTail
        prevalue=currentNode.val
        while(currentNode.next!=None):
            currentNode = currentNode.next
            self.assertTrue( (currentNode.val-prevalue)==1 )
            prevalue = currentNode.val

    def testListNode2(self):
        # Test Program
        # Initialize the test list:
        testHead = ListNode(4)
        node1 = ListNode(3)
        testHead.next = node1
        node2 = ListNode(2)
        node1.next = node2
        node3 = ListNode(1)
        node2.next = node3
        testTail = ListNode(0)
        node3.next = testTail


        testHead.reverseRecursively(testHead)

        currentNode = testTail
        prevalue=currentNode.val
        while(currentNode.next!=None):
            currentNode = currentNode.next
            self.assertTrue( (currentNode.val-prevalue)==1 )
            prevalue = currentNode.val
if __name__ == '__main__':
    unittest.main()
