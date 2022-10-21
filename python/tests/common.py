from array import ArrayType
import unittest

from typing import List, Optional
from src.common.listnode import ListNode


def array_to_listnode(arr: List) -> ListNode:
    curr = listnode = ListNode()
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return listnode.next

def listnode_to_array(l: ListNode) -> ArrayType:
    a = []
    while l:
        a.append(l.val)
        l = l.next
    return a
