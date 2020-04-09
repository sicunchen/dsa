// solution 1
var singleNumber = function(nums) {
  let set = new Set();
  for (n of nums) {
    if (!set.has(n)) {
      set.add(n);
    } else {
      set.delete(n);
    }
  }
  return set.values().next().value;
};

//solution 2
var singleNumber = function(nums) {
  let result = 0;
  for (n of nums) {
    result ^= n;
  }
  return result;
};
