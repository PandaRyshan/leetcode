from typing import Optional
from src.common.listnode import ListNode


class Solution:
    """
    l1 = [2, 4, 3], l2 = [5, 6, 4], output: [7, 0, 8]
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        curr = pre
        carry = 0
        while l1 or l2 or carry:
            res = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return pre.next
