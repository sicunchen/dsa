/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
  let [endLeft, endRight] = returnTwoPointers(s, 0, s.length - 1);
  if (endLeft >= endRight) {
    return true;
  }
  return (
    isPalindrome(s, endLeft + 1, endRight) ||
    isPalindrome(s, endLeft, endRight - 1)
  );
};

const isPalindrome = (s, left, right) => {
  const [endLeft, endRight] = returnTwoPointers(s, left, right);
  return endLeft >= endRight;
};

const returnTwoPointers = (s, left, right) => {
  while (left < right) {
    if (s[left] !== s[right]) {
      return [left, right];
    }
    left++;
    right--;
  }
  return [left, right];
};
