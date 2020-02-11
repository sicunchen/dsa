// solution 1
var majorityElement = function(nums) {
  let count = new Map();
  for (let n of nums) {
    if (!count.has(n)) {
      count.set(n, 0);
    }
    count.set(n, count.get(n) + 1);

    if (count.get(n) > nums.length / 2) {
      return n;
    }
  }
};

//solution 2
var majorityElement = function(nums) {
  nums.sort();
  return nums[Math.floor(nums.length / 2)];
};

// solution 3
var majorityElement = function(nums) {
  let maj;
  let count = 0;

  for (let n of nums) {
    if (count === 0) {
      maj = n;
    }
    if (n === maj) {
      count++;
    } else {
      count--;
    }
  }
  return maj;
};
