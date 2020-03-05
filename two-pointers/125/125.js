var isPalindrome = function(s) {
  if (s.length === 0) return true;
  let start = 0;
  let end = s.length - 1;
  while (start < end) {
    if (!s[start].match(/[0-9a-zA-Z]/)) {
      start++;
    } else if (!s[end].match(/[0-9a-zA-Z]/)) {
      end--;
    } else {
      if (s[start].toLowerCase() === s[end].toLowerCase()) {
        start++;
        end--;
      } else {
        return false;
      }
    }
  }
  return true;
};
