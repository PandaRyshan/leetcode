#![allow(dead_code)]
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut hashtable = std::collections::HashMap::<i32, i32>::new();
    for i in 0..nums.len() {
        if hashtable.contains_key(&(target - nums[i])) {
            return vec![hashtable[&(target - nums[i])], i as i32];
        }
        hashtable.insert(nums[i], i as i32);
    }
    return vec![];
}


#[cfg(test)]
mod tests {
    use std::vec;

    use super::two_sum;

    #[test]
    fn test_sum() {
        assert_ne!(two_sum(vec![2, 7, 11, 15], 11), vec![0, 1]);
        assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
        assert_eq!(two_sum(vec![5, 9, 6, 1, 3, 2, 2], 4), vec![3, 4]);
        assert_eq!(two_sum(vec![3, 3], 5), vec![]);
    }
}