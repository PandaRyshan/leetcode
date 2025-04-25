"""
https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

Leetcode 88. 合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2 ，以及两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你合并 nums1 和 nums2 ，合并后数组同样按 非递减顺序 排列，并返回合并后的数组。
请注意，最终的输出数组不应由函数返回，而是存储在数组 nums1 中。
nums1 的初始长度为 m + n ，其中前 m 个元素表示应合并的有效数字，后 n 个元素为 0 ，应忽略。
你必须在 O(1) 的额外空间复杂度下，原地 合并 nums1 和 nums2 。
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        #     return
        index_1, index_2 = m - 1, n - 1
        index_merged = m + n - 1
        while index_1 >= 0 and index_2 >= 0:
            if nums1[index_1] > nums2[index_2]:
                nums1[index_merged] = nums1[index_1]
                index_1 -= 1
            else:
                nums1[index_merged] = nums2[index_2]
                index_2 -= 1
            index_merged -= 1
    
        # Handle remaining elements in nums2
        while index_2 >= 0:
            nums1[index_merged] = nums2[index_2]
            index_2 -= 1
            index_merged -= 1

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1]

    nums1 = [2, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 5, 6, 8, 9]
    n = 5
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 5, 6, 8, 9]
