"""
1669. https://leetcode.cn/problems/merge-in-between-linked-lists/

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
from src.common.listnode import ListNode


class Solution:
    def merge_in_between(self, list1: ListNode, a: int,
                         b: int, list2: ListNode) -> ListNode:
        preA = list1
        for _ in range(a - 1):
            preA = preA.next

        preB = preA
        for _ in range(b - a + 2):
            preB = preB.next

        preA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = preB
        return list1
