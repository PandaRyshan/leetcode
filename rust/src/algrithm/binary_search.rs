#![allow(dead_code)]
pub fn binary_search(nums: Vec<i32>, target: i32) -> i32 {
    // return nums.binary_search(&target).map_or(-1, |x| x as i32);

    let mut start = 0;
    let mut end = nums.len() - 1;

    while start <= end {
        println!("start: {}, end: {}", start, end);
        let mid = (end - start) / 2 + start;
        println!("mid: {}", mid);
        if target > nums[mid] {
            start = mid + 1;
        }
        if target < nums[mid] {
            end = if mid > 0 { mid - 1 } else { break };
        }
        if target == nums[mid] {
            return mid as i32;
        }
    }

    return -1;
}


#[cfg(test)]
mod test {
    use super::binary_search;

    #[test]
    fn test_binary_search() {
        let mut res = binary_search(vec![5], -5);
        assert_eq!(-1, res);
        res = binary_search(vec![2, 5], 0);
        assert_eq!(-1, res);
    }
}