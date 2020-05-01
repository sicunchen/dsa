/**
 * @param nums: an integer array
 * @param target: An integer
 * @return: the difference between the sum and the target
 */
const twoSumClosest = function (nums, target) {
  nums.sort((a, b) => a - b);
  let left = 0;
  let right = nums.length - 1;
  let diff = Infinity;
  while (left < right) {
    const value = nums[left] + nums[right];
    if (value < target) {
      diff = Math.min(diff, target - value);
      left += 1;
    } else {
      diff = Math.min(diff, value - target);
      right -= 1;
    }
  }
  return diff;
};
