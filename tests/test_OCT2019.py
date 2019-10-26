from .context import OCT2019

from OCT2019.findLongestSubStringWithRepeatedCharacters import Solution2 as findLongestSubStringWithRepeatedCharacters

import unittest


class OCT2019Suite(unittest.TestCase):
    """Basic test cases."""

    def test_String1(self):
        solu = findLongestSubStringWithRepeatedCharacters()
        length = solu.lengthOfLongestSubstring("abrkaabcdefghijjxxx")

        self.assertEqual(length[0],10)
    def test_String2(self):
        solu = findLongestSubStringWithRepeatedCharacters()
        length = solu.lengthOfLongestSubstring("abcdddddfghjklmnbmhj")
        self.assertEqual(length[0], 10)


    def test_String3(self):
        solu = findLongestSubStringWithRepeatedCharacters()
        length = solu.lengthOfLongestSubstring("ABDEFGABEF")
        self.assertEqual(length[0], 6)


if __name__ == '__main__':
    unittest.main()
