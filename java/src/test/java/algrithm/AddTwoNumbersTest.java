package algrithm;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import common.ListNode;
import common.common;

public class AddTwoNumbersTest {
    
    @Test
    void testAddTwoNumbers() {
        AddTwoNumbers foo = new AddTwoNumbers();

        ListNode l1 = common.arrayToListNode(new int[] {2, 4, 3});
        ListNode l2 = common.arrayToListNode(new int[] {5, 6, 4});
        assertEquals(common.arrayToListNode(new int[] {7, 0, 8}), foo.addTwoNumbers(l1, l2));

        l1 = common.arrayToListNode(new int[] {9,9,9,9,9,9,9});
        l2 = common.arrayToListNode(new int[] {9,9,9,9});
        assertEquals(common.arrayToListNode(new int[] {8,9,9,9,0,0,0,1}), foo.addTwoNumbers(l1, l2));
    }
}
