import unittest

from src.group_anagrams_49 import Solution
from tests.common import sort_nested_list


class Test(unittest.TestCase):
    def test_group_anagrams(self):
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(sort_nested_list(expected), sort_nested_list(result))

        expected = [[""]]
        result = Solution().groupAnagrams([""])
        self.assertEqual(sort_nested_list(expected), sort_nested_list(result))
