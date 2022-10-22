from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (end - start) // 2 + start
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                start = mid + 1
            if target < nums[mid]:
                end = mid - 1

        return -1
