import unittest

from src.two_sum import Solution


class Test(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution().twoSum([5, 9, 6, 1, 3, 2, 2], 4), [3, 4])
        self.assertEqual(Solution().twoSum([5], 4), [])
