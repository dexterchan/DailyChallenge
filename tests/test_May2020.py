import unittest

from MAY2020.LRU_Cache import LRUCache


class May2020Suite(unittest.TestCase):
    def test_LRUCache(self):
        cache = LRUCache(2)

        cache.put(3, 3)
        cache.put(4, 4)
        self.assertEqual(3, cache.get(3))
        # 3
        self.assertIsNone(cache.get(2))
        # None
        cache.put(2, 2)
        self.assertIsNone(cache.get(4))
        # None (pre-empted by 2)
        self.assertEqual(3, cache.get(3))
        # 3

        self.assertEqual(2, cache.get(2))
        # 2
        cache.put(5, 5)
        self.assertIsNone(cache.get(3))
        # None

        print("next")
        cache = LRUCache(3)
        cache.put(3, 3)
        cache.put(4, 4)
        cache.put(2, 2)
        self.assertEqual(2, cache.get(2))
        # 2
        self.assertEqual(2, cache.get(2))
        # 2
        self.assertEqual(4, cache.get(4))
        # 4
        cache.put(10, 10)
        self.assertIsNone(cache.get(3))
        # None