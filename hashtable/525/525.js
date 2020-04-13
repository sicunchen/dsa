/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  let sumToIndex = new Map();
  let sum = 0;
  let ans = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i] === 0 ? -1 : 1;
    if (sum === 0) {
      ans = i + 1;
    }
    if (!sumToIndex.has(sum)) {
      sumToIndex.set(sum, i);
    } else {
      ans = Math.max(ans, i - sumToIndex.get(sum));
    }
  }
  return ans;
};
