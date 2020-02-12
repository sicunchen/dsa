var removeDuplicates = function(nums) {
  let uniqueIndex = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[uniqueIndex]) {
      nums[uniqueIndex + 1] = nums[i];
      uniqueIndex++;
    }
  }
  nums.splice(uniqueIndex + 1);
  return nums.length;
};
