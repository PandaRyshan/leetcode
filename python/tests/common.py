from array import ArrayType

from typing import List
from src.common.listnode import ListNode


def array_to_listnode(arr: List) -> ListNode:
    curr = listnode = ListNode()
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return listnode.next


def listnode_to_array(listnode: ListNode) -> ArrayType:
    a = []
    while listnode:
        a.append(listnode.val)
        listnode = listnode.next
    return a


def sort_nested_list(lst: List):
    return sorted(sorted(sublist) for sublist in lst)

