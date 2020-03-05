var isValid = function(s) {
  let stack = [];
  const match = { "{": "}", "}": "{", "[": "]", "]": "[", "(": ")", ")": "(" };

  for (let ch of s) {
    if (stack.length == 0 || ch !== match[stack[stack.length - 1]]) {
      stack.push(ch);
    } else {
      stack.pop();
    }
  }
  return stack.length === 0;
};
