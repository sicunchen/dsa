https://leetcode.com/problems/remove-duplicates-from-sorted-array/

[0,0,1,1,1,2,2,3,3,4] -> length=5

## Solution: two pointers

Because the array is sorted, we can use two pointers to track the current element and the unique element. As long as nums[uniq]==nums[curr], we increment curr to skip the duplicate. When nums[uniq]!=nums[curr], we copy the current value to nums[uniq+1], and increment uniq until we reach the end of nums.
