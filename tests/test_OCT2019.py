from .context import OCT2019

from OCT2019.findLongestSubStringWithRepeatedCharacters import Solution2 as findLongestSubStringWithRepeatedCharacters
from OCT2019.LongestPalindromicSubstring import Solution as LPSS

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


if __name__ == '__main__':
    unittest.main()
