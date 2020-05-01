/**
 * @param nums: an array of integer
 * @param target: An integer
 * @return: an integer
 */
const twoSum2 = function (nums, target) {
  nums.sort((a, b) => a - b);

  let left = 0;
  let right = nums.length - 1;

  let count = 0;
  while (left < right) {
    const value = nums[left] + nums[right];

    if (value <= target) {
      left += 1;
    } else {
      count += right - left;
      right -= 1;
    }
  }

  return count;
};
