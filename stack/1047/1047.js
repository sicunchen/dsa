var removeDuplicates = function(S) {
  let stack = [];
  for (let l of S) {
    if (stack[stack.length - 1] === l) {
      stack.pop();
    } else {
      stack.push(l);
    }
  }
  return stack.join("");
};
