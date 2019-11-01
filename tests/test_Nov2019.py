from .context import NOV2019
from NOV2019.TwoSum import two_sum


import unittest


class NOV2019Suite(unittest.TestCase):
    """Basic test cases."""

    def test_TwoSum(self):
        self.assertTrue(two_sum([4, 7, 1, -3, 2], 5))
        self.assertFalse(two_sum([4, 7, 1, -3, 2], 10))
        self.assertTrue(two_sum([4, 7, 2, -3, 2], 4))
        self.assertTrue(two_sum([4, 7, 2, -3, 2, 93], 90))