from .context import NOV2019
from NOV2019.TwoSum import two_sum, two_sum_HashSet
from NOV2019.SingleNumber import singleNumber

import unittest


class NOV2019Suite(unittest.TestCase):
    """Basic test cases."""

    def test_TwoSum(self):
        self.assertTrue(two_sum([4, 7, 1, -3, 2], 5))
        self.assertFalse(two_sum([4, 7, 1, -3, 2], 10))
        self.assertTrue(two_sum([4, 7, 2, -3, 2], 4))
        self.assertTrue(two_sum([4, 7, 2, -3, 2, 93], 90))

        self.assertTrue(two_sum_HashSet([4, 7, 2, -3, 2, 93], 90))
        self.assertTrue(two_sum_HashSet([4, 7, 1, -3, 2], 5))
        self.assertFalse(two_sum_HashSet([4, 7, 1, -3, 2], 10))
        self.assertTrue(two_sum_HashSet([4, 7, 2, -3, 2], 4))

    def testSingleNumber(self):
        r = singleNumber([4, 3, 2, 4, 1, 3, 2])
        self.assertIn(1, r)
        r = singleNumber([10,4, 3, 2, 4, 1, 3, 2])
        self.assertIn(10, r)
        self.assertIn(1, r)
        r = singleNumber([ 4, 3, 2, 4, 3, 2, 1])
        self.assertIn(1, r)