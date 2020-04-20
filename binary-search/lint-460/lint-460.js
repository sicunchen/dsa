const kClosestNumbers = function (A, target, k) {
  let result = [];
  let index = findFirst(A, target);
  let start = index - 1;
  let end = index;
  //use two pointers to populate the result
  for (let i = 0; i < k; i++) {
    if (start < 0) {
      result[i] = A[end];
      end++;
    } else if (end >= A.length) {
      result[i] = A[start];
      start--;
    } else {
      //put the closer number to the result, and move the corresponding pointer further
      if (target - A[start] <= A[end] - target) {
        result[i] = A[start];
        start--;
      } else {
        result[i] = A[end];
        end++;
      }
    }
  }
  return result;
};

//find the first position of the target or if the target doesn't exist, the first index of the  closest bigger number
const findFirst = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;
  while (start + 1 < end) {
    let mid = start + Math.floor((end - start) / 2);
    if (nums[mid] === target) {
      end = mid;
    } else if (nums[mid] < target) {
      start = mid;
    } else {
      end = mid;
    }
  }
  if (nums[start] >= target) {
    return start;
  } else if (nums[end] >= target) {
    return end;
  }
  return nums.length;
};
