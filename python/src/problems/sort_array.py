import random

from typing import List

class Solution:
    """Leetcode 912. 排序数组
    https://leetcode.cn/problems/sort-an-array/description/
    在不使用内置排序函数的情况下，给定一个整数数组 nums ，请你将该数组升序排列。
    必须在不使用任何内置函数的情况下解决问题，时间复杂度为 O(n log n)
    快排、归并、堆排
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sort an array of integers in ascending order. Do not use built-in sort functions.
        
        :param nums: List[int] - The input array of integers.
        :return: List[int] - The sorted array of integers.
        """
        print(self.quick_sort(nums))
        print(self.merge_sort(nums))
        print(self.quick_sort_in_place(nums, 0, len(nums) - 1))
        # print(self.heap_sort(nums))


    def quick_sort(self, nums: List[int]) -> List[int]:
        """
        find a pivot and partition the array into three parts,
        elements less than the pivot, elements equal to the pivot,
        and elements greater than the pivot. Then recursively sort
        the left and right parts.
        """
        if len(nums) <= 1:
            return nums
        pivot_index = random.randint(0, len(nums) - 1)
        pivot_value = nums[pivot_index]
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot_value:
                less.append(num)
            elif num == pivot_value:
                equal.append(num)
            else:
                greater.append(num)
        return self.quick_sort(less) + equal + self.quick_sort(greater)


    def quick_sort_in_place(self, nums: List[int], left: int, right: int) -> List[int]:
        """
        In-place quick sort algorithm with three-way partitioning to handle
        duplicates efficiently. This implementation handles arrays with many
        duplicate values much better than standard quicksort.
        """
        if left >= right:
            return nums
            
        # Choose random pivot to avoid worst-case performance
        pivot_index = random.randint(left, right)
        pivot_value = nums[pivot_index]
        
        # Three-way partitioning: elements < pivot | elements == pivot | elements > pivot
        lt_index = left      # Less than: everything to the left of lt is less than pivot
        gt_index = right     # Greater than: everything to the right of gt is greater than pivot
        current_index = left       # Current element being examined
        
        while current_index <= gt_index:
            if nums[current_index] < pivot_value:
                nums[lt_index], nums[current_index] = nums[current_index], nums[lt_index]
                lt_index += 1
                current_index += 1
            elif nums[current_index] > pivot_value:
                nums[current_index], nums[gt_index] = nums[gt_index], nums[current_index]
                gt_index -= 1
                # Don't increment i here as we need to examine the swapped element
            else:
                current_index += 1
                
        # Recursively sort the partitions
        self.quick_sort_in_place(nums, left, lt_index - 1)
        self.quick_sort_in_place(nums, gt_index + 1, right)
        return nums
        

    def heap_sort(self, nums: List[int]) -> List[int]:

        pass



    def merge_sort(self, nums: List[int]) -> List[int]:
        """
        Merge sort is a divide-and-conquer algorithm that divides the array
        into two halves, recursively sorts them, and then merges the sorted
        halves. It has a time complexity of O(n log n) and is stable.
        """
        self.recursion_divided_partition(nums, 0, len(nums) - 1)
        return nums

    def recursion_divided_partition(self, nums: List[int], left: int, right: int) -> List[int]:
        """
        Split the array into two halves and recursively sort each half.
        The base case is when the left index is greater than or equal to
        the right index, in which case the array is already sorted.
        """
        if left >= right:
            return nums[left:right + 1]

        mid = left + (right - left) // 2
        self.recursion_divided_partition(nums, left, mid)
        self.recursion_divided_partition(nums, mid + 1, right)
        self.sort_and_merge(nums, left, mid, right)

    def sort_and_merge(self, nums: List[int], left: int, mid: int, right: int) -> List[int]:
        """
        Merge two sorted subarrays into a single sorted array.
        Update the original array with the sorted elements.
        """
        result = []
        index_left = left
        index_right = mid + 1

        while index_left <= mid and index_right <= right:
            if nums[index_left] <= nums[index_right]:
                result.append(nums[index_left])
                index_left += 1
            else:
                result.append(nums[index_right])
                index_right += 1

        while index_left <= mid:
            result.append(nums[index_left])
            index_left += 1

        while index_right <= right:
            result.append(nums[index_right])
            index_right += 1

        nums[left : right + 1] = result


if __name__ == "__main__":
    s = Solution()

    nums = [5, 2, 3, 1]
    s.sortArray(nums)

    nums = [5, 1, 1, 2, 0, 0]
    s.sortArray(nums)

    nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    s.sortArray(nums)
