mod two_sum;
mod add_two_numbers;
mod binary_search;
mod array_strings_are_equal;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }

}

pub fn vec_to_listnode(v: Vec<i32>) -> Option<Box<ListNode>> {
    let mut prev = Some(Box::new(ListNode::new(0)));
    let mut curr = &mut prev;
    for val in v {
        curr.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
        curr = &mut curr.as_mut().unwrap().next;
    }

    return prev.unwrap().next;
}