// 基于中心点枚举
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  if (!s) {
    return s;
  }
  let longest = 0;
  let start = 0;
  for (let middle = 0; middle < s.length; middle++) {
    const oddCenterLen = getPalindromeLength(s, middle, middle);
    const evenCenterLen = getPalindromeLength(s, middle, middle + 1);
    if (oddCenterLen > longest) {
      longest = oddCenterLen;
      start = middle - Math.floor(longest / 2);
    }
    if (evenCenterLen > longest) {
      longest = evenCenterLen;
      start = middle - Math.floor(longest / 2) + 1;
    }
  }
  return s.substring(start, start + longest);
};

const getPalindromeLength = (s, left, right) => {
  while (left >= 0 && right < s.length && s[left] == s[right]) {
    left--;
    right++;
  }
  return right - left - 1;
};
