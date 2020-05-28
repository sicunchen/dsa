//1
var longestPalindrome = function (s) {
  let count = {};
  let ans = 0;
  let oddCount = 0;
  for (let l of s) {
    if (!count[l]) {
      count[l] = 0;
    }
    count[l]++;
  }
  for (let freq of Object.values(count)) {
    if (freq % 2 === 0) {
      ans += freq;
    } else {
      ans += freq - 1;
      oddCount++;
    }
  }
  return oddCount > 0 ? ans + 1 : ans;
};

var longestPalindrome = function (s) {
  let set = new Set();
  for (let l of s) {
    if (set.has(l)) {
      set.delete(l);
    } else {
      set.add(l);
    }
  }
  return set.size > 0 ? s.length - set.size + 1 : s.length;
};
