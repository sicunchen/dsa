var strStr = function (haystack, needle) {
  if (!needle) {
    return 0;
  }
  for (let i = 0; i < haystack.length - needle.length + 1; i++) {
    let notEqual = false;
    for (let j = 0; j < needle.length; j++) {
      if (haystack[i + j] !== needle[j]) {
        notEqual = true;
        break;
      }
    }
    if (!notEqual) return i;
  }
  return -1;
};
