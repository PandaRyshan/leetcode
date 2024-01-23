import unittest

from src.merge_in_between_linked_list import Solution
from tests.common import array_to_listnode, listnode_to_array


class Test(unittest.TestCase):

    def test_merge_in_between_linked_list(self):
        list1 = array_to_listnode([0, 1, 2, 3, 4, 5, 6])
        list2 = array_to_listnode([1000000, 1000001, 1000002, 1000003, 1000004])
        expected = array_to_listnode([0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])
        result = Solution().merge_in_between(list1, 2, 5, list2)
        self.assertEqual(listnode_to_array(expected), listnode_to_array(result))
