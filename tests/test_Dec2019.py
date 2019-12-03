from DEC2019.TrappingRainwater import capacity as trapwatercapacity
from DEC2019.BuddyStrings import Solution as buddyStringSolu
import unittest


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