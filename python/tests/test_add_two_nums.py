import unittest

from src.add_two_nums import Solution
from tests.common import array_to_listnode, listnode_to_array


class Test(unittest.TestCase):

    def test_add_two_nums(self):
        expected = array_to_listnode([7, 0, 8])
        result = Solution().addTwoNumbers(array_to_listnode([2, 4, 3]),
                                          array_to_listnode([5, 6, 4]))
        self.assertEqual(listnode_to_array(expected), listnode_to_array(result))

        expected = array_to_listnode([8, 9, 9, 9, 0, 0, 0, 1])
        l1 = array_to_listnode([9, 9, 9, 9, 9, 9, 9])
        l2 = array_to_listnode([9, 9, 9, 9])
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(listnode_to_array(expected), listnode_to_array(result))
