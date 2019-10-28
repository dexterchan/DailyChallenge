from .context import OCT2019

from OCT2019.findLongestSubStringWithRepeatedCharacters import Solution2 as findLongestSubStringWithRepeatedCharacters
from OCT2019.LongestPalindromicSubstring import Solution as LPSS
from OCT2019.ValidateBalancedParentheses import Solution as BP

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




if __name__ == '__main__':
    unittest.main()
