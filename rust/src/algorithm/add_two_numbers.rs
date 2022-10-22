#![allow(dead_code)]

use crate::ListNode;
pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut l1 = l1;
    let mut l2 = l2;
    let mut prev = Some(Box::new(ListNode::new(0)));
    let mut curr = &mut prev;
    let mut carry: i32 = 0;

    while l1 != None || l2 != None || carry != 0 {
        let sum = match l1 {Some(ref l) => l.val, None => 0} +
                       match l2 {Some(ref l) => l.val, None => 0} + carry;
        carry = sum / 10;
        curr.as_mut().unwrap().next = Some(Box::new(ListNode::new(sum % 10)));
        curr = &mut curr.as_mut().unwrap().next;
        l1 = match l1 { Some(l1) => l1.next, None => None};
        l2 = match l2 { Some(l2) => l2.next, None => None};
    }

    return prev.unwrap().next;
}


#[cfg(test)]
mod test {
    use crate::{algorithm::vec_to_listnode};

    use super::add_two_numbers;
    #[test]
    fn test_add_two_numbers() {
        let l1 = vec_to_listnode(vec![9, 9, 9, 9, 9, 9, 9]);
        let l2 = vec_to_listnode(vec![9, 9, 9, 9]);
        let l3 = vec_to_listnode(vec![2, 4, 3]);
        let l4 = vec_to_listnode(vec![5, 6, 4]);

        let foo = add_two_numbers(l1, l2);
        let bar = add_two_numbers(l3, l4);
        assert_eq!(vec_to_listnode(vec![8, 9, 9, 9, 0, 0, 0, 1]), foo);
        assert_eq!(vec_to_listnode(vec![7, 0, 8]), bar);
    }
}
