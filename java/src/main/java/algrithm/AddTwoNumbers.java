package algrithm;

import common.ListNode;

/**
 * url: https://leetcode.cn/problems/add-two-numbers/
 */

public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode prev = new ListNode();
        ListNode curr = prev;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sumVal = (l1 != null ? l1.getVal() : 0) + (l2 != null ? l2.getVal() : 0) + carry;
            carry = sumVal / 10;
            curr.setNext(new ListNode(sumVal % 10));
            curr = curr.getNext();
            l1 = l1 != null ? l1.getNext() : null;
            l2 = l2 != null ? l2.getNext() : null;
        }

        return prev.getNext();
    }
}
