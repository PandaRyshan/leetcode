package common;

public class common {
    public static ListNode arrayToListNode(int[] arr) {
        ListNode prev = new ListNode();
        ListNode curr = prev;
        for (int val : arr) {
            curr.next = new ListNode(val);
            curr = curr.next;
        }

        return prev.getNext();
    }

}
