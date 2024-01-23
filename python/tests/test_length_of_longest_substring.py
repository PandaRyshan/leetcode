import unittest

from src.length_of_longest_substring_3 import Solution


class Test(unittest.TestCase):

    def test_length_of_longest_substring(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, Solution().lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, Solution().lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(7, Solution().lengthOfLongestSubstring("abcdabefg"))
