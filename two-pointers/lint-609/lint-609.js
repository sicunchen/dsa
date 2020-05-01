const twoSum5 = function (nums, target) {
  //注意js sort时最好写一个comparator函数
  nums.sort((a, b) => a - b);

  let left = 0;
  let right = nums.length - 1;

  let count = 0;
  while (left < right) {
    const value = nums[left] + nums[right];

    if (value > target) {
      right -= 1;
    } else {
      count += right - left;
      left += 1;
    }
  }

  return count;
};
