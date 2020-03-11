// solution 1
var postorderTraversal = function(root) {
  let result = [];
  const traverse = (root, result) => {
    if (!root) return;
    traverse(root.left, result);
    traverse(root.right, result);
    result.push(root.val);
  };
  traverse(root, result);
  return result;
};

// solution 2
var postorderTraversal = function(root) {
  let result = [];
  let stack = [];
  if (root) stack.push(root);
  while (stack.length !== 0) {
    const curr = stack.pop();
    result.push(curr.val);
    if (curr.left) stack.push(curr.left);
    if (curr.right) stack.push(curr.right);
  }
  return result.reverse();
};


//solution 3
var postorderTraversal = function (root) {
    let result = [];
    let stack = [];
    if (root) stack.push([root, false]);
    while (stack.length !== 0) {
        const [curr, visited] = stack.pop();
        if (visited) {
            result.push(curr.val);
        } else {
            stack.push([curr, true]);
            if (curr.right) stack.push([curr.right, false]);
            if (curr.left) stack.push([curr.left, false]);
        }

    }
    return result;
};