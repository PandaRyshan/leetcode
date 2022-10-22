package algorithm;

public class BinarySearch {
    public int search(int[] nums, int target) {
        int start = 0, end = nums.length - 1;

        while (start <= end) {
            int mid = (end - start) / 2 + start;

            if (target > nums[mid]) {
                start = mid + 1;
            }
            if (target < nums[mid]) {
                end = mid - 1;
            }
            if (target == nums[mid]) {
                return mid;
            }
        }

        return -1;
    }
    
}
