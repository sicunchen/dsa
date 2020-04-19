//This doesn't pass for some reason. Need more clarification
const findPosition = function (nums, target) {
  if (!nums || !nums.length) return -1;
  let start = 0;
  let end = nums.length - 1;
  while (start + 1 < end) {
    let mid = start + Math.floor((end - start) / 2);
    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      start = mid;
    } else {
      end = mid;
    }
  }

  if (nums[start] === target) {
    return start;
  }
  if (nums[end] === target) {
    return end;
  }
  return -1;
};

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
  if (nums[start] === target) {
    return start;
  } else if (nums[end] === target) {
    return end;
  }
  return -1;
};

const findLast = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;

  while (start + 1 < end) {
    let mid = start + Math.floor((end - start) / 2);
    if (nums[mid] === target) {
      start = mid;
    } else if (nums[mid] < target) {
      start = mid;
    } else {
      end = mid;
    }
  }
  if (nums[end] === target) {
    return end;
  } else if (nums[start] === target) {
    return start;
  }
  return -1;
};

const findRange = function (nums, target) {
  let start, end, mid;
  let bound = new Array(2);
  if (nums.length === 0) {
    bound[0] = -1;
    bound[1] = -1;
    return bound;
  }
  //search for left bound
  start = 0;
  end = nums.length - 1;
  while (start + 1 < end) {
    mid = start + Math.floor((end - start) / 2);
    if (nums[mid] === target) {
      end = mid;
    } else if (nums[mid] < target) {
      start = mid;
    } else {
      end = mid;
    }
  }
  if (nums[start] === target) {
    bound[0] = start;
  } else if (nums[end] === target) {
    bound[0] = end;
  } else {
    bound[0] = bound[1] = -1;
    return bound;
  }
  //search for right bound
  start = 0;
  end = nums.length - 1;
  while (start + 1 < end) {
    mid = start + Math.floor((end - start) / 2);
    if (nums[mid] === target) {
      start = mid;
    } else if (nums[mid] < target) {
      start = mid;
    } else {
      end = mid;
    }
  }
  if (nums[end] === target) {
    bound[1] = end;
  } else if (nums[start] === target) {
    bound[1] = start;
  } else {
    bound[1] = bound[1] = -1;
    return bound;
  }
  return bound;
};
