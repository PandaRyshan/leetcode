fn main() {
    let nums = [2, 7, 11, 15, 23];
    let target = 9;
    let mut hashtable = std::collections::HashMap::<i32, i32>::new();
    for i in 0..nums.len() {
        if hashtable.contains_key(&(target - nums[i])) {
            println!("{}, {}", nums[i], i);
            return [nums[i], i];
        }
        hashtable.insert(nums[i], i);
    }
    return [];
}
