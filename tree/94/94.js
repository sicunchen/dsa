// solution 1
var inorderTraversal = function(root) {
  let result = [];
  const traverse = root => {
    if (!root) return;
    traverse(root.left);
    result.push(root.val);
    traverse(root.right);
  };

  traverse(root);
  return result;
};

// solution 2
var inorderTraversal = function(root) {
  let result = [];
  let stack = [];
  let curr = root;
  while (stack.length !== 0 || curr !== null) {
    while (curr !== null) {
      stack.push(curr);
      curr = curr.left;
    }
    curr = stack.pop();
    result.push(curr.val);
    curr = curr.right;
  }
  return result;
};
