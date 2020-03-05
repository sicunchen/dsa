var twoSum = function(nums, target) {
  let map = new Map();
  let result = [];
  for (let [i, num] of nums.entries()) {
    if (map.get(target - num) !== undefined) {
      return [i, map.get(target - num)];
    }

    map.set(num, i);
  }
};
