// solution 1
var rotate = function(nums, k) {
  let extra = [];
  for (let i = 0; i < nums.length; i++) {
    extra[(i + k) % nums.length] = nums[i];
  }
  for (let i = 0; i < nums.length; i++) {
    nums[i] = extra[i];
  }
};

// solution 2
var rotate = function(nums, k) {
  const reverse = (arr, start, end) => {
    while (start < end) {
      let temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
  };
  // if we rotate an array equal to its size, it will turn out to be the same, so we only need to take effective steps.
  //if size=5, for k=3 and k=8, the array will be the same after rotation
  k = k % nums.length;
  reverse(nums, 0, nums.length - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, nums.length - 1);
};
