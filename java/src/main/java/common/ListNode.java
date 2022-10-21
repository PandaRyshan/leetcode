package common;

@lombok.Data
public class ListNode {
    int val;
    ListNode next;

    public ListNode() {}

    public ListNode(int val) {this.val = val;}

    public ListNode(int val, ListNode next) {this.val = val; this.next = next;}
    
    public boolean equals(ListNode l1, ListNode l2) {
        while (l1 != null || l2 != null) {
            if ((l1 == null && l2 != null) ||
                (l1 != null && l2 == null)) {
                    return false;
                }
            return l1.getVal() == l2.getVal();
        }
        return l1 == l2;
    }
}
