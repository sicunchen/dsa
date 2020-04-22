const searchBigSortedArray = function (reader, target) {
  // write your code here
  let kth = 1;
  while (reader.get(kth - 1) < target) {
    kth = kth * 2;
  }
  let start = 0;
  let end = kth - 1;

  while (start + 1 < end) {
    let mid = start + Math.floor((end - start) / 2);
    if (target > reader.get(mid)) {
      start = mid;
    } else {
      end = mid;
    }
  }
  if (reader.get(start) === target) {
    return start;
  } else if (reader.get(end) === target) {
    return end;
  }
  return -1;
};
